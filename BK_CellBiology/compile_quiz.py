import json
import random
import glob
import os

def compile_quiz():
    source_dir = 'quiz/BK_finalterm'
    output_file = os.path.join(source_dir, 'compiled_random_quiz.json')
    
    # Get all json files in the directory
    json_files = glob.glob(os.path.join(source_dir, '*.json'))
    
    # Exclude the output file if it already exists to avoid recursive issues
    if output_file in json_files:
        json_files.remove(output_file)
    
    compiled_questions = []
    
    print(f"Found {len(json_files)} source files.")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                
            if not isinstance(questions, list):
                print(f"Skipping {file_path}: Root element is not a list.")
                continue
                
            # Randomly select 10 questions, or all if less than 10
            num_questions = len(questions)
            if num_questions > 10:
                selected_questions = random.sample(questions, 10)
            else:
                selected_questions = questions
                
            print(f"Selected {len(selected_questions)} questions from {os.path.basename(file_path)}")
            
            # Add source info (optional, but helpful for debugging/context)
            for q in selected_questions:
                # Create a copy to avoid modifying the original if we were keeping it in memory
                q_copy = q.copy() 
                # q_copy['source_file'] = os.path.basename(file_path) # Uncomment if source tracking is desired
                compiled_questions.append(q_copy)
                
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file_path}")
        except Exception as e:
            print(f"An error occurred processing {file_path}: {e}")

    # Shuffle the final compiled list so topics are mixed
    random.shuffle(compiled_questions)
    
    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(compiled_questions, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully compiled {len(compiled_questions)} questions into {output_file}")
    except Exception as e:
        print(f"Failed to write output file: {e}")

if __name__ == "__main__":
    compile_quiz()
