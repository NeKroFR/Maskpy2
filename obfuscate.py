import py_compile
from blake3 import blake3
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
import os

def obfuscate(filename):
    i = 0
    tmpfilename = '.tmp'
    while os.path.exists(tmpfilename+'.pyc'):
        tmpfilename = '.tmp' + str(i)
    tmpfilename = tmpfilename + '.pyc'

    with open (py_compile.compile('test.py', cfile=tmpfilename), "rb") as f:
        bytecode = f.read()
    os.remove(tmpfilename)

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
    exec(marshal.loads(plaintext[16:]))"""
    return code
