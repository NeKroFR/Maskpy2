def with_defaults(a: int, b: int = 10, c: str = "hello") -> str:
    return c * a + str(b)

def with_args(*args, **kwargs):
    total = 0
    for x in args:
        total += x
    for k, v in kwargs.items():
        total += v
    return total

def nested_func(n: int) -> int:
    def inner(x):
        return x * 2
    result = 0
    for i in range(n):
        result += inner(i)
    return result

def with_lambda(items: list) -> list:
    fn = lambda x: x ** 2
    return [fn(i) for i in items]

def multi_return(x: int) -> int:
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x < 10:
        return 1
    else:
        return 2

def with_try(a: int, b: int) -> int:
    try:
        return a // b
    except ZeroDivisionError:
        return -1

def with_while_break(n: int) -> int:
    total = 0
    i = 0
    while True:
        if i >= n:
            break
        total += i
        i += 1
        if total > 100:
            break
    return total

def with_continue(n: int) -> int:
    total = 0
    for i in range(n):
        if i % 3 == 0:
            continue
        total += i
    return total

def with_nested_loops(n: int) -> int:
    total = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            total += i * j
    return total

def with_comprehension(n: int) -> list:
    return [x * 2 for x in range(n) if x % 2 == 0]

def with_dict_ops(data: dict) -> int:
    result = 0
    for k in data:
        result += data[k]
    return result

def with_string_ops(s: str) -> str:
    parts = s.split(" ")
    reversed_parts = []
    for p in parts:
        reversed_parts.append(p[::-1])
    return " ".join(reversed_parts)

def with_bool_logic(a: bool, b: bool) -> int:
    if a and not b:
        return 1
    elif b and not a:
        return 2
    elif a and b:
        return 3
    return 0

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    errors = 0

    # defaults
    assert with_defaults(3) == "hellohellohello10", f"defaults: {with_defaults(3)}"
    assert with_defaults(2, 5, "x") == "xx5", f"defaults2: {with_defaults(2, 5, 'x')}"

    # *args **kwargs
    assert with_args(1, 2, 3) == 6
    assert with_args(1, x=10, y=20) == 31

    # nested function
    assert nested_func(5) == 20

    # lambda
    assert with_lambda([1, 2, 3]) == [1, 4, 9]

    # multi return
    assert multi_return(-5) == -1
    assert multi_return(0) == 0
    assert multi_return(5) == 1
    assert multi_return(50) == 2

    # try/except
    assert with_try(10, 3) == 3
    assert with_try(10, 0) == -1

    # while + break
    assert with_while_break(10) == 45
    assert with_while_break(20) == 105

    # continue
    assert with_continue(10) == 27

    # nested loops
    assert with_nested_loops(4) == 22

    # comprehension
    assert with_comprehension(8) == [0, 4, 8, 12]

    # dict ops
    assert with_dict_ops({"a": 1, "b": 2, "c": 3}) == 6

    # string ops
    assert with_string_ops("hello world test") == "olleh dlrow tset"

    # bool logic
    assert with_bool_logic(True, False) == 1
    assert with_bool_logic(False, True) == 2
    assert with_bool_logic(True, True) == 3
    assert with_bool_logic(False, False) == 0

    # fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765

    print("all edge case tests passed")
