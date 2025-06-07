def X1(X5: str, X11: bytes) -> str:
    X3 = 0
    X4 = 0
    X8 = 0
    X6 = 14
    X7 = 0
    while (X6 != (- 1)):
        if (X6 == 14):
            X6 = 13
        elif (X6 == 13):
            X9 = X5
            X6 = 12
        elif (X6 == 12):
            X10 = X11
            X6 = 11
        elif (X6 == 11):
            X4 = 42
            X6 = 10
        elif (X6 == 10):
            X8 = X11.decode('utf-8')
            X6 = 9
        elif (X6 == 9):
            if ((X4 | (X4 & 2880989662)) == X4):
                X6 = 0
            else:
                X6 = 8
        elif (X6 == 8):
            X3 = (X4 & (X4 - 68))
            X6 = 7
        elif (X6 == 7):
            X3 = (X3 - (X3 & 11))
            X6 = 6
        elif (X6 == 6):
            X3 = (X3 * 38030)
            X6 = 5
        elif (X6 == 5):
            X3 = (X3 ^ 58237)
            X6 = 4
        elif (X6 == 4):
            X3 = (X3 & (X3 - 224))
            X6 = 3
        elif (X6 == 3):
            if (((X4 + 3) - 3) == X4):
                X6 = 1
            else:
                X6 = 2
        elif (X6 == 2):
            pass
            X6 = (- 1)
        elif (X6 == 1):
            pass
            X6 = (- 1)
        elif (X6 == 0):
            X7 = ((X5 + ' ') + X8)
            X6 = (- 1)
    return X7

def X2(X13):
    if (X13 == 0):
        return b'\x00'
    X12 = bytearray()
    while X13:
        X12.append((X13 & 255))
        X13 >>= 8
    return bytes(X12[::(- 1)])
print('Hello, my name is', (X1('John', b'Doe') + '.'))