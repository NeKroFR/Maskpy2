import py_compile, os


def load_bin(file_path):
    pyc_path = py_compile.compile(file_path)

    with open(pyc_path, "rb") as f:
        raw_bin = f.read()
    os.remove(pyc_path)
    return raw_bin

def obfuscate(file_path):
    raw_bin = load_bin(file_path)

    raw_bin = ''.join(format(byte, '08b') for byte in raw_bin).replace("0"," ").replace("1"," ᠍") # https://invisible-characters.com/

    code = f"""import marshal as m
exec(m.loads(bytes(int("{raw_bin}".replace(" ","0").replace(" ᠍","1")[i:i+8],2)for i in range(0,len("{raw_bin}".replace(" ","0").replace(" ᠍","1")),8))[16:]))
"""
    return code

