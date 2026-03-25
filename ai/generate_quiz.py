import os
import json
import google.generativeai as genai
import argparse
import sys
import time

# ================= CONFIGURATION =================
# API Key (Best practice: set this in your environment variables)
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE" 
API_KEY = os.environ.get("GEMINI_API_KEY")
# =================================================

def setup_gemini():
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please export it in your shell: export GEMINI_API_KEY='your_key'")
        return None
    genai.configure(api_key=API_KEY)
    # Using the current available model
    return genai.GenerativeModel('gemini-3-flash-preview')

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
    # Remove ```json and ``` or just ```
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    
    if text.endswith("```"):
        text = text[:-3]
    
    return text.strip()

def generate_quiz(model, content_or_file):
    """
    Generates a quiz using either a string (markdown/text) or a Gemini File object (PDF).
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
       - ~10 Hard Questions (Specific details, complex application, dates/history)
    4. **Constraints:**
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

    if isinstance(content_or_file, str):
        prompt_parts = [f"{prompt_instructions}\n\n**Input Material:**\n{content_or_file}"]
    else:
        # It's a Gemini File object
        prompt_parts = [content_or_file, prompt_instructions]

    print("Sending request to Gemini... (this might take a minute for 40 questions)")
    try:
        response = model.generate_content(prompt_parts)
        return clean_json_response(response.text)
    except Exception as e:
        print(f"API Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate quizzes from study guides or PDFs using Gemini.")
    parser.add_argument("sources", nargs="*", help="Path to one or more source files (Markdown or PDF)")
    args = parser.parse_args()

    if not args.sources:
        parser.print_help()
        sys.exit(0)

    model = setup_gemini()
    if not model:
        return

    for source_path in args.sources:
        print(f"\n--- Processing: {source_path} ---")
        
        is_pdf = source_path.lower().endswith('.pdf')
        content_to_send = None

        if is_pdf:
            print(f"Uploading PDF: {source_path}")
            try:
                content_to_send = genai.upload_file(source_path, mime_type="application/pdf")
                while content_to_send.state.name == "PROCESSING":
                    time.sleep(2)
                    content_to_send = genai.get_file(content_to_send.name)
            except Exception as e:
                print(f"Error uploading PDF: {e}")
                continue
        else:
            content_to_send = read_content(source_path)
            if not content_to_send:
                continue

        # Determine output path
        base_name = os.path.splitext(os.path.basename(source_path))[0]
        # Standardized output dir based on original script
        output_dir = "_quiz"
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, f"{base_name}.json")

        json_str = generate_quiz(model, content_to_send)
        
        if json_str:
            try:
                # Validate JSON
                quiz_data = json.loads(json_str)
                
                print(f"Successfully generated {len(quiz_data)} questions.")

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    json.dump(quiz_data, f, indent=2, ensure_ascii=False)
                
                print(f"Quiz saved to: {os.path.abspath(output_file_path)}")
                
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON from model response for {source_path}.")
                print("Raw output start:", json_str[:100])
                print("Error:", e)
                # Save raw output for debugging
                debug_file = f"debug_raw_{base_name}.txt"
                with open(debug_file, "w") as f:
                    f.write(json_str)
                print(f"Raw output saved to {debug_file}")
        
        # Cleanup uploaded file if it's a PDF
        if is_pdf and content_to_send:
            try:
                genai.delete_file(content_to_send.name)
            except:
                pass

if __name__ == "__main__":
    main()
