#!/bin/bash

# Configuration
API_KEY="${GEMINI_API_KEY}"
MODEL_NAME="gemini-2.5-flash-lite"
INPUT_FILE="${1:-revision_material.pdf}"
OUTPUT_FILE="${2:-revision_ocr.md}"
BATCH_SIZE=5
DELAY_SECONDS=5

# Rate limit handling
RETRY_DELAY_INITIAL=10 # Initial delay in seconds for rate limit retries
MAX_RETRIES=5 # Maximum number of retries for rate limit errors

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
for cmd in jq curl pdfinfo qpdf; do
    if ! command -v $cmd &> /dev/null;
    then
        echo -e "${YELLOW}Error: '$cmd' is not installed.${NC}"
        echo "Please install it via: sudo apt install poppler-utils qpdf jq curl"
        exit 1
    fi
done

if [ -z "$API_KEY" ]; then
    echo -e "${YELLOW}Error: GEMINI_API_KEY is not set.${NC}"
    echo "Usage: export GEMINI_API_KEY='your_key_here'"
    exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${YELLOW}Error: File '$INPUT_FILE' not found.${NC}"
    exit 1
fi

# Get total pages
TOTAL_PAGES=$(pdfinfo "$INPUT_FILE" | grep "Pages:" | awk '{print $2}')
echo -e "${BLUE}Total Pages: $TOTAL_PAGES${NC}"

# Determine start page & handle output file
START_PAGE=1
if [ -f "$OUTPUT_FILE" ]; then
    # Extract the last processed page number from the file comments
    LAST_PAGE=$(grep -oE "<!-- Batch: Pages [0-9]+-([0-9]+) -->" "$OUTPUT_FILE" | tail -n 1 | sed -E 's/.*-([0-9]+) -->/\1/')
    
    if [ -n "$LAST_PAGE" ]; then
        START_PAGE=$((LAST_PAGE + 1))
        echo -e "${BLUE}Found existing progress. Resuming from page $START_PAGE...${NC}"
    else
        echo -e "${BLUE}Output file exists but is empty or has no markers. Starting fresh.${NC}"
        > "$OUTPUT_FILE"
    fi
else
    echo -e "${BLUE}Starting fresh task. Initialized: $OUTPUT_FILE${NC}"
    > "$OUTPUT_FILE"
fi

if [ "$START_PAGE" -gt "$TOTAL_PAGES" ]; then
    echo -e "${GREEN}All pages already processed ($TOTAL_PAGES total).${NC}"
    exit 0
fi

# Function to delete remote file
cleanup_remote_file() {
    local file_name="$1"
    # echo "Cleaning up remote file: $file_name"
    curl -s -X DELETE "https://generativelanguage.googleapis.com/v1beta/files/$file_name?key=$API_KEY" > /dev/null
}

# Loop through pages
for (( start=START_PAGE; start<=TOTAL_PAGES; start+=BATCH_SIZE )); do
    end=$((start + BATCH_SIZE - 1))
    if [ $end -gt $TOTAL_PAGES ]; then
        end=$TOTAL_PAGES
    fi

    echo -e "\n${GREEN}Processing Batch: Pages $start to $end...${NC}"
    
    CHUNK_FILE="temp_chunk_${start}_${end}.pdf"

    # Extract pages
    qpdf --empty --pages "$INPUT_FILE" $start-$end -- "$CHUNK_FILE" 2>/dev/null

    if [ ! -f "$CHUNK_FILE" ]; then
        echo "Error: Failed to create chunk file."
        continue
    fi

    FILE_SIZE=$(wc -c < "$CHUNK_FILE")
    MIME_TYPE="application/pdf"

    # Upload
    # echo "Uploading..."
    UPLOAD_RESPONSE=$(curl -s -X POST \
        -H "X-Goog-Upload-Protocol: raw" \
        -H "X-Goog-Upload-Header-Content-Length: $FILE_SIZE" \
        -H "X-Goog-Upload-Header-Content-Type: $MIME_TYPE" \
        -H "Content-Type: $MIME_TYPE" \
        --data-binary "@$CHUNK_FILE" \
        "https://generativelanguage.googleapis.com/upload/v1beta/files?key=$API_KEY")

    FILE_URI=$(echo "$UPLOAD_RESPONSE" | jq -r '.file.uri')
    FILE_NAME_ID=$(echo "$UPLOAD_RESPONSE" | jq -r '.file.name' | cut -d'/' -f2) # Extract ID part if needed, usually it's 'files/ID'

    if [ "$FILE_URI" == "null" ] || [ -z "$FILE_URI" ]; then
        echo "Upload failed."
        rm "$CHUNK_FILE"
        continue
    fi

    # Wait for processing
    # echo "Waiting for processing..."
    STATE="PROCESSING"
    while [ "$STATE" != "ACTIVE" ]; do
        CHECK_RESPONSE=$(curl -s "https://generativelanguage.googleapis.com/v1beta/files/$FILE_NAME_ID?key=$API_KEY")
        STATE=$(echo "$CHECK_RESPONSE" | jq -r '.state')
        
        if [ "$STATE" == "FAILED" ]; then
            echo "File processing failed."
            cleanup_remote_file "$FILE_NAME_ID"
            rm "$CHUNK_FILE"
            continue 2
        fi
        
        if [ "$STATE" != "ACTIVE" ]; then
            sleep 1
        fi
    done

    # Generate Content with retry logic
    RETRY_COUNT=0
    while true; do
        # Generate Content
        # echo "Requesting OCR..."
        GENERATE_DATA=$(jq -n \
                      --arg uri "$FILE_URI" \
                      --arg mime "$MIME_TYPE" \
                      '{ 
                        contents: [{ 
                          parts: [ 
                            { file_data: { mime_type: $mime, file_uri: $uri } }, 
                            { text: "Transcribe the text from these pages into Markdown format exactly as it appears in the original language (Vietnamese). Do not translate. Identify headers and paragraphs correctly. Ignore page numbers at the bottom of the pages. Do not add excessive newlines between paragraphs." } 
                          ] 
                        }] 
                      }')

        GENERATE_RESPONSE_RAW=$(curl -s -X POST \
            -H "Content-Type: application/json" \
            -d "$GENERATE_DATA" \
            "https://generativelanguage.googleapis.com/v1beta/models/$MODEL_NAME:generateContent?key=$API_KEY")

        # Check for API error
        ERROR_MESSAGE=$(echo "$GENERATE_RESPONSE_RAW" | jq -r '.error.message')
        ERROR_CODE=$(echo "$GENERATE_RESPONSE_RAW" | jq -r '.error.status')

        if [[ "$ERROR_CODE" == "RESOURCE_EXHAUSTED" || "$ERROR_MESSAGE" == *"quota"* || "$ERROR_MESSAGE" == *"rate limit"* ]]; then
            RETRY_COUNT=$((RETRY_COUNT + 1))
            if [ "$RETRY_COUNT" -le "$MAX_RETRIES" ]; then
                CURRENT_RETRY_DELAY=$((RETRY_DELAY_INITIAL * (2 ** (RETRY_COUNT - 1))))
                echo -e "${YELLOW}Rate limit hit for batch $start-$end. Retrying in ${CURRENT_RETRY_DELAY} seconds... (Attempt $RETRY_COUNT/$MAX_RETRIES)${NC}"
                sleep "$CURRENT_RETRY_DELAY"
                continue # Retry the API call
            else
                echo -e "${YELLOW}Max retries (${MAX_RETRIES}) reached for rate limit on batch $start-$end. Exiting.${NC}"
                echo "Raw response: $GENERATE_RESPONSE_RAW"
                rm "$CHUNK_FILE"
                cleanup_remote_file "$FILE_NAME_ID"
                exit 1
            fi
        fi
        
        # If no rate limit or other API error (assuming error.message would catch others)
        TEXT_CONTENT=$(echo "$GENERATE_RESPONSE_RAW" | jq -r '.candidates[0].content.parts[0].text')
        
        if [ "$TEXT_CONTENT" != "null" ] && [ -n "$TEXT_CONTENT" ]; then
            # Successfully got content, break retry loop
            break
        else
            # Other errors (e.g., content filtering, no text, or API returned success but empty content)
            echo "Error: No content returned for pages $start-$end or other non-rate-limit API error."
            echo "Debug (full response): $GENERATE_RESPONSE_RAW"
            rm "$CHUNK_FILE"
            cleanup_remote_file "$FILE_NAME_ID"
            exit 1
        fi
    done

    if [ "$TEXT_CONTENT" != "null" ] && [ -n "$TEXT_CONTENT" ]; then
        # Header for the batch in the output file
        echo -e "\n\n<!-- Batch: Pages $start-$end -->\n" >> "$OUTPUT_FILE"
        echo "$TEXT_CONTENT" >> "$OUTPUT_FILE"
        
        # Display to user immediately
        echo -e "${YELLOW}--- Output for Pages $start-$end ---${NC}"
        echo "$TEXT_CONTENT"
        echo -e "${YELLOW}-----------------------------------${NC}"
    else
        # This else block is mostly redundant now due to the retry loop's exit conditions,
        # but kept for safety in case TEXT_CONTENT becomes null after break (unlikely).
        echo "Final check failed for content extraction on pages $start-$end."
        rm "$CHUNK_FILE"
        cleanup_remote_file "$FILE_NAME_ID"
        exit 1
    fi

    # Cleanup
    rm "$CHUNK_FILE"
    cleanup_remote_file "$FILE_NAME_ID"

    if [ $end -lt $TOTAL_PAGES ]; then
        echo "Waiting $DELAY_SECONDS seconds..."
        sleep $DELAY_SECONDS
    fi
done

echo -e "\n${GREEN}Full OCR complete. Saved to $OUTPUT_FILE${NC}"