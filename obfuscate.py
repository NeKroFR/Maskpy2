import py_compile
from blake3 import blake3
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
from strip import strip
import os

def get_code(filename):
    # return the code from a python script
    with open(filename, 'r') as f:
        code = f.read()
    return code

def get_bytecode(code):
    # Return bytecode from a python script
    i = 0
    tmp = '.tmp.py'
    while os.path.exists(tmp):
        tmp = f'.tmp{i}.py'
        i += 1

    tmpfilename = tmp + 'c'
    try:
        with open(tmp, 'w') as f:
            f.write(code)
        with open(py_compile.compile(tmp, cfile=tmpfilename), "rb") as f:
            bytecode = f.read()
        return bytecode
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
        if os.path.exists(tmpfilename):
            os.remove(tmpfilename)

def crypto_checksum(bytecode):
    # Return a python script which performs a Blake3 checksum
    # of the bytecode and encrypts it with ChaCha20-Poly1305
    checksum = blake3(bytecode).hexdigest()
    key = get_random_bytes(32)
    nonce = get_random_bytes(24)
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(bytecode)
    code = f"""import marshal
from blake3 import blake3
from Crypto.Cipher import ChaCha20_Poly1305

plaintext = ChaCha20_Poly1305.new(key={key}, nonce={nonce}).decrypt_and_verify({ciphertext}, {tag})
if blake3(plaintext).hexdigest() == '{checksum}':
    exec(marshal.loads(plaintext[16:]))
"""
    return code

def obfuscate(filename):
    code = get_code(filename)
    code = strip(code)
    bytecode = get_bytecode(code)
    code = crypto_checksum(bytecode)
    code = strip(code)
    return code
