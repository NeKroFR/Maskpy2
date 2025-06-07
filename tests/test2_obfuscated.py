def X2(X4: str, X6: bytes) -> str:
    X3 = 0
    X7 = 0
    X12 = 0
    X10 = 0
    X8 = 10
    X9 = 0
    while (X8 != (- 1)):
        if (X8 == 10):
            X8 = 9
        elif (X8 == 9):
            X5 = X4
            X8 = 8
        elif (X8 == 8):
            X11 = X6
            X8 = 7
        elif (X8 == 7):
            X7 = 42
            X8 = 6
        elif (X8 == 6):
            X3 = bytearray(X4.encode('utf-8'))
            X8 = 5
        elif (X8 == 5):
            for X12 in range(len(X3)):
                X3[X12] ^= X6[(X12 % len(X6))]
            X8 = 4
        elif (X8 == 4):
            if ((X7 ^ X7) == 0):
                X8 = 0
            else:
                X8 = 3
        elif (X8 == 3):
            X10 = 0
            X8 = 2
        elif (X8 == 2):
            X10 = (X10 ^ 7363)
            X8 = 1
        elif (X8 == 1):
            X10 = (X10 * 47907)
            X8 = (- 1)
        elif (X8 == 0):
            X9 = X3.decode('utf-8')
            X8 = (- 1)
    return X9

def X1(X14):
    if (X14 == 0):
        return b'\x00'
    X13 = bytearray()
    while X14:
        X13.append((X14 & 255))
        X14 >>= 8
    return bytes(X13[::(- 1)])
print('Hello, my name is', (X2('xwethgcx', b'2\x18\r\x1aH#\x0c\x1d') + '.'))