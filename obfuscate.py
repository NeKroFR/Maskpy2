import py_compile
from blake3 import blake3
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
from strip import strip
import os


def get_bytecode(filename):
    # Return bytecode from a pythonn script
    i = 0
    tmpfilename = '.tmp'
    while os.path.exists(tmpfilename+'.pyc'):
        tmpfilename = '.tmp' + str(i)
    tmpfilename = tmpfilename + '.pyc'

    with open (py_compile.compile('test.py', cfile=tmpfilename), "rb") as f:
        bytecode = f.read()
    os.remove(tmpfilename)
    return bytecode

def crypto_checksum(bytecode):
    # Return a python script wich perform a Blake3 checksum
    # of the bytecode and encrypt it with ChaCha20-Poly1305
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
    # TODO: strip before getting the bytecode, may do a tempfile (be sure the file does not exist)
    bytecode = get_bytecode(filename)
    code = crypto_checksum(bytecode)
    code = strip(code)
    return code
