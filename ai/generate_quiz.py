import os
import json
import argparse
import sys
import time
from google import genai
from google.genai import types

# ================= CONFIGURATION =================
API_KEY = os.environ.get("GEMINI_API_KEY")
# =================================================

def setup_client():
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please export it in your shell: export GEMINI_API_KEY='your_key'")
        return None
    return genai.Client(api_key=API_KEY)

def read_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def clean_json_response(text):
    """
    Cleans the response text to ensure it's valid JSON.
    Removes markdown code blocks if present.
    """
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    
    if text.endswith("```"):
        text = text[:-3]
    
    return text.strip()

def generate_quiz(client, contents):
    """
    Generates a quiz using a list of contents (strings/markdown/text or Gemini File objects).
    """
    prompt_instructions = """
    You are an expert educational content creator.
    Create a comprehensive 40-question multiple-choice quiz based strictly on the provided material.
    
    **Requirements:**
    1. **Format:** Return strictly a valid JSON array of objects. No extra text, markdown, or explanations.
    2. **Quantity:** Generate roughly 40 questions depending on the length of the material coverage.
    3. **Difficulty Distribution:**
       - ~10 Easy Questions (Definitions, basic facts)
       - ~20 Medium Questions (Comparisons, functions, advantages/disadvantages)
       - ~10 Hard Questions (Specific details, complex application, reasoning/interdependencies)
    4. **Constraints:**
       - **Avoidance**: Do NOT include questions about specific obscure historical dates, history facts, or highly specific/obscure species-related numbers (e.g., precise elemental percentages of a very specific strain unless it's a major generalizable concept). Focus on high-level understanding and process interdependencies.
       - **Limit "All of the above":** Use this option sparingly (max 3-4 times).
       - **"shuffleOptions" Tag:**
         - Default to `true`.
         - Set to `false` ONLY if the options contain relative references like "All of the above", "Both A and B", "None of the above", or specific sequences (e.g. chronological order).
       - **Coverage:** Ensure questions cover ALL sections of the text.
    
    **JSON Schema:**
    [
      {
        "question": "Question text string",
        "options": [
          "Option 1",
          "Option 2",
          "Option 3",
          "Option 4"
        ],
        "answer": "The correct option string (must match exactly one option)",
        "shuffleOptions": true
      }
    ]
    """

    prompt_parts = [prompt_instructions]
    for i, content in enumerate(contents):
        if isinstance(content, str):
            prompt_parts.append(f"\n\n**Input Material {i+1} (Text/Markdown):**\n{content}")
        else:
            # It's a Gemini File object (from client.files.upload)
            prompt_parts.append(content)

    print("Sending request to Gemini... (this might take a minute for 40 questions)")
    try:
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt_parts,
            config=types.GenerateContentConfig(
                temperature=0.2,
            )
        )
        return clean_json_response(response.text)
    except Exception as e:
        print(f"API Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate quizzes from study guides and PDFs using the modern Gemini SDK.")
    parser.add_argument("sources", nargs="*", help="Path to one or more source files (Markdown or PDF)")
    args = parser.parse_args()

    if not args.sources:
        parser.print_help()
        sys.exit(0)

    client = setup_client()
    if not client:
        return

    all_contents = []
    source_names = []
    uploaded_files = []

    print(f"--- Preparing {len(args.sources)} source(s) ---")

    for source_path in args.sources:
        is_pdf = source_path.lower().endswith('.pdf')
        source_names.append(os.path.splitext(os.path.basename(source_path))[0])

        if is_pdf:
            print(f"Uploading PDF: {source_path}")
            try:
                # The modern SDK uses 'file' instead of 'path'
                uploaded_file = client.files.upload(file=source_path)
                
                # Wait for processing
                while uploaded_file.state.name == "PROCESSING":
                    time.sleep(2)
                    uploaded_file = client.files.get(name=uploaded_file.name)
                
                if uploaded_file.state.name == "FAILED":
                    print(f"File processing failed for {source_path}")
                    continue
                    
                all_contents.append(uploaded_file)
                uploaded_files.append(uploaded_file)
            except Exception as e:
                print(f"Error uploading PDF: {e}")
        else:
            content = read_content(source_path)
            if content:
                all_contents.append(content)
            else:
                print(f"Skipping empty or missing file: {source_path}")

    if not all_contents:
        print("No valid content found to process.")
        return

    # Determine output path - use the first source name
    output_name = source_names[0] if source_names else "quiz_" + str(int(time.time()))
    
    output_dir = "_quiz"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f"{output_name}.json")

    json_str = generate_quiz(client, all_contents)
    
    if json_str:
        try:
            quiz_data = json.loads(json_str)
            print(f"Successfully generated {len(quiz_data)} questions.")

            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(quiz_data, f, indent=2, ensure_ascii=False)
            
            print(f"Quiz saved to: {os.path.abspath(output_file_path)}")
            
        except json.JSONDecodeError as e:
            print("Failed to decode JSON from model response.")
            print("Raw output start:", json_str[:200])
            print("Error:", e)
            debug_file = f"debug_raw_{combined_name}.txt"
            with open(debug_file, "w") as f:
                f.write(json_str)
            print(f"Raw output saved to {debug_file}")
    
    # Cleanup uploaded files
    for f in uploaded_files:
        try:
            client.files.delete(name=f.name)
            print(f"Deleted remote file: {f.name}")
        except Exception as e:
            print(f"Error deleting file {f.name}: {e}")

if __name__ == "__main__":
    main()
