import os
import json
import google.generativeai as genai
import re

# ================= CONFIGURATION =================
# Path to the study material file
SOURCE_FILE = "./_study_guide/Chapter01-02.IntroductionBasicConcepts.md" 

# Output file name
OUTPUT_FILE = "quiz.json"

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

def generate_quiz(model, content):
    prompt = f"""
    You are an expert educational content creator.
    Create a comprehensive 40-question multiple-choice quiz based strictly on the provided text.
    
    **Input Text:**
    {content}

    **Requirements:**
    1. **Format:** Return strictly a valid JSON array of objects. No extra text, markdown, or explanations.
    2. **Quantity:** Generate more or equal to 40 questions.
    3. **Difficulty Distribution:**
       - ~10 Easy Questions (Definitions, basic facts)
       - ~20 Medium Questions (Comparisons, functions, advantages/disadvantages)
       - ~10 Hard Questions (Specific details, complex application, dates/history)
    4. **Constraints:**
       - **Limit "All of the above":** Use this option sparingly (max 3-4 times).
       - **"shuffleOptions" Tag:**
         - Default to `true`.
         - Set to `false` ONLY if the options contain relative references like "All of the above", "Both A and B", "None of the above", or specific sequences (e.g. chronological order).
       - **Coverage:** Ensure questions cover ALL sections of the text (Intro, Biomass, Enzymes, Metabolites, History table, Methods).
    
    **JSON Schema:**
    [
      {{
        "question": "Question text string",
        "options": [
          "Option 1",
          "Option 2",
          "Option 3",
          "Option 4"
        ],
        "answer": "The correct option string (must match exactly one option)",
        "shuffleOptions": true
      }}
    ]
    """

    print("Sending request to Gemini... (this might take a minute for 40 questions)")
    try:
        response = model.generate_content(prompt)
        return clean_json_response(response.text)
    except Exception as e:
        print(f"API Error: {e}")
        return None

def main():
    model = setup_gemini()
    if not model:
        return

    print(f"Reading file: {SOURCE_FILE}")
    content = read_content(SOURCE_FILE)
    if not content:
        return

    # Determine output path
    base_name = os.path.splitext(os.path.basename(SOURCE_FILE))[0]
    output_dir = "_quiz"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f"{base_name}.json")

    json_str = generate_quiz(model, content)
    
    if json_str:
        try:
            # Validate JSON
            quiz_data = json.loads(json_str)
            
            print(f"Successfully generated {len(quiz_data)} questions.")

            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(quiz_data, f, indent=2)
            
            print(f"Quiz saved to: {os.path.abspath(output_file_path)}")
            
        except json.JSONDecodeError as e:
            print("Failed to decode JSON from model response.")
            print("Raw output start:", json_str[:100])
            print("Error:", e)
            # Save raw output for debugging
            with open("debug_raw_output.txt", "w") as f:
                f.write(json_str)

if __name__ == "__main__":
    main()
