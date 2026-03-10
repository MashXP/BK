import os
import argparse
from pypdf import PdfReader, PdfWriter

def split_pdfs(source_dir, dest_dir, batch_size):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")

    files = [f for f in os.listdir(source_dir) if f.lower().endswith('.pdf')]
    files.sort()

    if not files:
        print(f"No PDF files found in '{source_dir}'.")
        return

    print(f"Found files: {files}")

    for filename in files:
        filepath = os.path.join(source_dir, filename)
        print(f"Processing {filepath}...")
        try:
            reader = PdfReader(filepath)
            num_pages = len(reader.pages)
            
            # Clean filename for output
            base_name = os.path.splitext(filename)[0].replace(' ', '_')
            
            for i in range(0, num_pages, batch_size):
                writer = PdfWriter()
                start_page = i
                end_page = min(i + batch_size, num_pages)
                
                for page_num in range(start_page, end_page):
                    page = reader.pages[page_num]
                    writer.add_page(page)
                    
                output_filename = f"{base_name}_part_{int(i/batch_size)+1}.pdf"
                output_filepath = os.path.join(dest_dir, output_filename)
                
                # Set compression level when writing
                with open(output_filepath, "wb") as f_out:
                    writer.write(f_out)
                print(f"  Created: {output_filename} (Pages {start_page+1}-{end_page})")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split and compress PDFs in a directory into smaller chunks.")
    parser.add_argument("source_dir", help="Directory containing PDF files to split")
    parser.add_argument("--dest_dir", default="_temp", help="Directory to save split files (default: _temp)")
    parser.add_argument("--batch_size", type=int, default=5, help="Number of pages per split file (default: 5)")
    
    args = parser.parse_args()
    
    split_pdfs(args.source_dir, args.dest_dir, args.batch_size)