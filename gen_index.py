import os

def create_index_file(target_dir):
    # Only process the target directory, no recursion
    root = os.path.abspath(target_dir)
    folder_name = os.path.basename(root)
    
    if not folder_name:
        return

    # Filter for markdown files in the current directory
    files = os.listdir(root)
    md_files = [f for f in files if f.endswith('.md') and os.path.isfile(os.path.join(root, f))]
    
    # Determine the name of the index file to be created
    index_filename = f"{folder_name}.md"
    
    # Check if there are any md files to list (other than the index itself)
    files_to_list = [f for f in md_files if f != index_filename]
    
    if not files_to_list:
        print(f"No markdown files to list in {root}")
        return
        
    # Prepare content
    # 1. Header using folder name
    # 2. List of [[file.md]]
    lines = [f"# {folder_name}\n"]
    
    # Sort files to ensure deterministic order
    files_to_list.sort()
    
    for md_file in files_to_list:
        lines.append(f"- [[{md_file}]]")
        
    content = "\n".join(lines) + "\n"
    
    # Write the file
    output_path = os.path.join(root, index_filename)
    try:
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"Generated index: {output_path}")
    except IOError as e:
        print(f"Error writing to {output_path}: {e}")

if __name__ == "__main__":
    # Target the current directory only
    target_dir = "."
    create_index_file(target_dir)
