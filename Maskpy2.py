import sys
import argparse
from obfuscate import obfuscate

def save_file(code, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print("\033[1;32mSuccess:\033[0m the file has been successfully obfuscated")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obfuscate Python code.")
    parser.add_argument("input_file", help="The Python file to obfuscate.")
    parser.add_argument("-o", "--output", help="The output file name. Defaults to input_file_obfuscated.py")
    parser.add_argument("-f", "--functions", nargs="*", help="Functions to obfuscate. If not provided or empty, obfuscates everything.")
    args = parser.parse_args()
    filename = args.input_file
    if not filename.endswith(".py"):
        print("\033[91mError: \033[0myou need to choose a python file!")
        sys.exit(1)
    if args.output:
        obfuscated_filename = args.output
    else:
        obfuscated_filename = filename[:-3] + "_obfuscated.py"
    functions_to_obfuscate = args.functions or []
    try:
        obfuscated = obfuscate(filename, functions_to_obfuscate)
        save_file(obfuscated, obfuscated_filename)
    except FileNotFoundError:
        print("\033[91mError: \033[0mfile doesn’t exist!")
        sys.exit(1)
    except ValueError as e:
        print(f"\033[91mError: \033[0m{e}")
        sys.exit(1)
