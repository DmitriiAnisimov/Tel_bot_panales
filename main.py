import subprocess
import sys

def run_script(script_path):
    """Run a Python script using subprocess."""
    python_executable = sys.executable  # This gets the path to the current Python interpreter
    subprocess.run([python_executable, script_path])

def main():
    # Run dia.py
    run_script("dia/dia.py")  # Change this to the correct path

    # Run jumbo.py
    run_script("jumbo/jumbo.py")  # Change this to the correct path

    # Run carrefour.py
    run_script("carrefour/carrefour.py")  # Change this to the correct path

    # Run carrefour.py
    run_script("farmacity/farmacity.py")  # Change this to the correct path

    # Run join_csv.py
    run_script("join_csv.py")  # Change this to the correct path

    # Run prepare.py
    run_script("prepare.py")  # Change this to the correct path

    # Run sql_script.py
    run_script("sql_script.py")  # Change this to the correct path

if __name__ == "__main__":
    main()
