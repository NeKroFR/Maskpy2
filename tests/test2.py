
def get_sol(name: str, key: bytes) -> str:
    name_bytes = bytearray(name.encode('utf-8'))
    for i in range(len(name_bytes)):
        name_bytes[i] ^= key[i % len(key)]
    return name_bytes.decode('utf-8')

print("Hello, my name is", get_sol("xwethgcx", b'2\x18\r\x1aH#\x0c\x1d') + ".")
