from random import randint, shuffle

def get_sol(a, b):
    if b < a:
        a, b = b, a
    
    c = randint(1, 10) * a
    d = c - a
    arr = [a, b, c, d]
    shuffle(arr)
    return arr[0] + arr[1] - arr[2] - arr[3] % (a + b)

a = randint(1, 10)

print("Hello,", end=" ")
print(f"the solution is {get_sol(randint(40,140), randint(40,140)) + a}.")
