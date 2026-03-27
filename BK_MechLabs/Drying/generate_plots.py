import subprocess
import os
import sys

def run_script(script_path):
    print(f"Running {script_path}...")
    try:
        subprocess.run([sys.executable, script_path], check=True) 
        print(f"Successfully finished {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

if __name__ == "__main__":
    scripts = [
        "Scripts/plot_curves.py",
        "Scripts/plot_exp_curves.py",
        "Scripts/plot_exp_rate_curves.py"
    ]
    
    for script in scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"Warning: {script} not found.")
    
    print("\nAll plots should be generated in the 'Images/' directory.")
