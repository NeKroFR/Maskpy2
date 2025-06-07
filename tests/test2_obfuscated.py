def X2(X10: str, X6: bytes) -> str:
    X9 = 0
    X4 = 0
    X5 = 0
    X3 = 7
    X11 = 0
    while (X3 != (- 1)):
        if (X3 == 7):
            X3 = 6
        elif (X3 == 6):
            X8 = X10
            X3 = 5
        elif (X3 == 5):
            X7 = X6
            X3 = 4
        elif (X3 == 4):
            X4 = 42
            X3 = 3
        elif (X3 == 3):
            X9 = X6.decode('utf-8')
            X3 = 2
        elif (X3 == 2):
            if ((((((X4 & 970071477) | (X4 & (~ 970071477))) == X4) or ((X4 & 4294967295) == X4)) and (((X4 & 4082411376) | (X4 & (~ 4082411376))) == X4)) and (((((X4 & 1463618901) | (X4 & (~ 1463618901))) == X4) or ((X4 & 4294967295) == X4)) or ((X4 & 4294967295) == X4))):
                X3 = 0
            else:
                X3 = 1
        elif (X3 == 1):
            X5 = (X4 + 294384078)
            X3 = (- 1)
        elif (X3 == 0):
            X11 = ((X10 + ' ') + X9)
            X3 = (- 1)
    return X11

def X1(X13):
    if (X13 == 0):
        return b'\x00'
    X12 = bytearray()
    while X13:
        X12.append((X13 & 255))
        X13 >>= 8
    return bytes(X12[::(- 1)])
print('Hello, my name is', (X2('John', b'Doe') + '.'))