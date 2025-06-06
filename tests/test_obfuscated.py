from random import randint as X000004, shuffle as X000001

def X000003(X000005):
    X000006 = (X000004(1, 10) * X000005)
    X000007 = (X000006 - X000005)
    X000008 = [X000005, X000006, X000007]
    X000001(X000008)
    return ((X000008[0] + X000008[1]) - X000008[2])
X000002 = X000004(1, 10)
print('Hello,', end=' ')
print(f'the solution is {(X000003(X000004(40, 140)) + X000002)}.')