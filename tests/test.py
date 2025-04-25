from random import randint, shuffle

def get_sol(a):
    b = randint(1, 10) * a
    c = b - a
    arr = [a, b, c]
    shuffle(arr)
    return arr[0] + arr[1] - arr[2]

a = randint(1, 10)

print("Hello,", end=" ")
print(f"the solution is {get_sol(randint(40,140)) + a}.")
