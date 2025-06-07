
def get_sol(name: str, first_name: bytes)-> str:
    first_name_str = first_name.decode('utf-8')
    return name + " " + first_name_str

print("Hello, my name is", get_sol("John", b"Doe") + ".")