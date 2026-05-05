# pure python crypto primitives for vm layer

MASK64 = 0xFFFFFFFFFFFFFFFF
MASK32 = 0xFFFFFFFF


# --- xoshiro256** ---

def rotl(x, k):
    return ((x << k) | (x >> (64 - k))) & MASK64


def _splitmix64(state):
    state = (state + 0x9E3779B97F4A7C15) & MASK64
    z = state
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
    return state, (z ^ (z >> 31)) & MASK64


def xoshiro256_init(seed):
    # expand seed via splitmix64
    state = [0] * 4
    s = seed & MASK64
    for i in range(4):
        s, state[i] = _splitmix64(s)
    return state


def xoshiro256_next(state):
    # xoshiro256** algorithm
    result = (rotl((state[1] * 5) & MASK64, 7) * 9) & MASK64
    t = (state[1] << 17) & MASK64
    state[2] ^= state[0]
    state[3] ^= state[1]
    state[1] ^= state[2]
    state[0] ^= state[3]
    state[2] ^= t
    state[3] = rotl(state[3], 45)
    return result


def xoshiro256_stream(state, n):
    # generate n bytes of keystream
    out = bytearray()
    while len(out) < n:
        val = xoshiro256_next(state)
        out.extend(val.to_bytes(8, 'little'))
    return bytes(out[:n])


# --- xtea ---

def xtea_encrypt(v0, v1, key):
    delta = 0x9E3779B9
    s = 0
    for _ in range(32):
        v0 = (v0 + ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (s + key[s & 3]))) & MASK32
        s = (s + delta) & MASK32
        v1 = (v1 + ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (s + key[(s >> 11) & 3]))) & MASK32
    return v0, v1


def xtea_decrypt(v0, v1, key):
    delta = 0x9E3779B9
    s = (delta * 32) & MASK32
    for _ in range(32):
        v1 = (v1 - ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (s + key[(s >> 11) & 3]))) & MASK32
        s = (s - delta) & MASK32
        v0 = (v0 - ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (s + key[s & 3]))) & MASK32
    return v0, v1


def xtea_encrypt_bytes(data, key):
    # pad to 8-byte blocks, ecb mode
    pad_len = (8 - len(data) % 8) % 8
    data = data + b'\x00' * pad_len
    out = bytearray()
    for i in range(0, len(data), 8):
        v0 = int.from_bytes(data[i:i+4], 'big')
        v1 = int.from_bytes(data[i+4:i+8], 'big')
        ev0, ev1 = xtea_encrypt(v0, v1, key)
        out.extend(ev0.to_bytes(4, 'big'))
        out.extend(ev1.to_bytes(4, 'big'))
    return bytes(out)


def xtea_decrypt_bytes(data, key):
    out = bytearray()
    for i in range(0, len(data), 8):
        v0 = int.from_bytes(data[i:i+4], 'big')
        v1 = int.from_bytes(data[i+4:i+8], 'big')
        dv0, dv1 = xtea_decrypt(v0, v1, key)
        out.extend(dv0.to_bytes(4, 'big'))
        out.extend(dv1.to_bytes(4, 'big'))
    return bytes(out)


# --- siphash-2-4 ---

def sipround(v0, v1, v2, v3):
    v0 = (v0 + v1) & MASK64
    v1 = rotl(v1, 13)
    v1 ^= v0
    v0 = rotl(v0, 32)
    v2 = (v2 + v3) & MASK64
    v3 = rotl(v3, 16)
    v3 ^= v2
    v0 = (v0 + v3) & MASK64
    v3 = rotl(v3, 21)
    v3 ^= v0
    v2 = (v2 + v1) & MASK64
    v1 = rotl(v1, 17)
    v1 ^= v2
    v2 = rotl(v2, 32)
    return v0, v1, v2, v3


def siphash(key_bytes, data):
    # siphash-2-4 with 128-bit key
    k0 = int.from_bytes(key_bytes[0:8], 'little')
    k1 = int.from_bytes(key_bytes[8:16], 'little')

    v0 = k0 ^ 0x736f6d6570736575
    v1 = k1 ^ 0x646f72616e646f6d
    v2 = k0 ^ 0x6c7967656e657261
    v3 = k1 ^ 0x7465646279746573

    length = len(data)
    # pad data to process full 8-byte words
    padded = data + b'\x00' * (8 - (length % 8) if length % 8 else 0)

    # process full 8-byte blocks
    block_count = length // 8
    for i in range(block_count):
        m = int.from_bytes(padded[i*8:(i+1)*8], 'little')
        v3 ^= m
        for _ in range(2):
            v0, v1, v2, v3 = sipround(v0, v1, v2, v3)
        v0 ^= m

    # last block with length byte
    last = bytearray(8)
    remaining = length % 8
    for i in range(remaining):
        last[i] = data[block_count * 8 + i]
    last[7] = length & 0xFF
    m = int.from_bytes(last, 'little')

    v3 ^= m
    for _ in range(2):
        v0, v1, v2, v3 = sipround(v0, v1, v2, v3)
    v0 ^= m

    # finalization
    v2 ^= 0xFF
    for _ in range(4):
        v0, v1, v2, v3 = sipround(v0, v1, v2, v3)

    return (v0 ^ v1 ^ v2 ^ v3) & MASK64


def derive_vm_key(master_seed, siphash_key, vm_id):
    data = master_seed.to_bytes(8, 'little') + vm_id.to_bytes(2, 'little')
    h1 = siphash(siphash_key, data)
    h2 = siphash(siphash_key, h1.to_bytes(8, 'little'))
    return (h1 & MASK32, (h1 >> 32) & MASK32, h2 & MASK32, (h2 >> 32) & MASK32)


if __name__ == '__main__':
    # test xoshiro256
    state = xoshiro256_init(12345)
    vals = [xoshiro256_next(state) for _ in range(5)]
    assert all(isinstance(v, int) and 0 <= v <= MASK64 for v in vals)
    assert len(set(vals)) == 5
    stream = xoshiro256_stream(xoshiro256_init(12345), 100)
    assert len(stream) == 100

    # test xtea round-trip
    key = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)
    v0, v1 = 0xDEADBEEF, 0xCAFEBABE
    ev0, ev1 = xtea_encrypt(v0, v1, key)
    dv0, dv1 = xtea_decrypt(ev0, ev1, key)
    assert (dv0, dv1) == (v0, v1)
    # bytes round-trip
    data = b'hello world! this is a test of xtea encryption'
    encrypted = xtea_encrypt_bytes(data, key)
    assert encrypted != data
    decrypted = xtea_decrypt_bytes(encrypted, key)
    assert decrypted[:len(data)] == data

    # test siphash
    key_bytes = bytes(range(16))
    h1 = siphash(key_bytes, b'')
    h2 = siphash(key_bytes, b'hello')
    h3 = siphash(key_bytes, b'hello')
    assert isinstance(h1, int)
    assert h2 == h3
    assert h1 != h2
    assert h1 != 0

    # test key derivation
    k = derive_vm_key(12345, key_bytes, 0)
    k2 = derive_vm_key(12345, key_bytes, 1)
    assert len(k) == 4 and all(isinstance(x, int) for x in k)
    assert k != k2
    print('all crypto tests passed')
