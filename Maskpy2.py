import sys
from obfuscate import obfuscate

def gui(): # Shall I remove the banner?
    banner = """\033[92m                                ▄▄▄▄ 
                                   █ 
    ▗▖▗▞▀▜▌ ▄▄▄ █  ▄ ▗▄▄▖ ▄   ▄ █▀▀▀ 
▐▛▚▞▜▌▝▚▄▟▌▀▄▄  █▄▀  ▐▌ ▐▌█   █ █▄▄▄
▐▌  ▐▌     ▄▄▄▀ █ ▀▄ ▐▛▀▘  ▀▀▀█ 
▐▌  ▐▌          █  █ ▐▌   ▄   █ 
                           ▀▀▀"""
    print(banner)
    filename = input("""\033[1;35mDrag the file to be obfuscated here : \033[0m""")
    if filename[0] == filename[-1]:
        if filename[0] == "'" or filename[0] == '"':
            filename = filename[1:-1]

    return filename

def open_file(filename):
    if filename[-3:] != ".py":
        print("\033[91mError: \033[0myou need to choose a python file!")
        sys.exit()
    try:
        f = open(filename, "r", encoding='utf-8')
        content = f.read()
        cuted_file = content.splitlines()
        return cuted_file 
    except:
        print("\033[91mError: \033[0mfile doesn't exist!")
        sys.exit()

def save_file(code, filename):
    f = open(filename, "w",encoding="utf-8")
    f.write(code)
    print("\033[1;32mSuccess:\033[0m the file has been successfully obfuscated")


if __name__ == "__main__":
    if sys.platform != "linux":
        print("\033[91mError: \033[0mThis script must be run on a Linux system!")
        print("The obfuscated file can be run on any system.")
        sys.exit()

    a = len(sys.argv)
    if a == 1:
        filename = gui()
        obfuscated_filename = filename[:-3]+"_obfuscated.py"        
    elif a == 2:
        filename = sys.argv[1]
        obfuscated_filename = filename[:-3]+"_obfuscated.py"
    elif a == 3:
        filename = sys.argv[1]
        obfuscated_filename = sys.argv[2]
    else:
        print("Error: too many arguments")
        exit()
    obfuscated = obfuscate(filename)
    save_file(obfuscated, obfuscated_filename)
