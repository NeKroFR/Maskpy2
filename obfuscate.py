import ast
from strip import strip

def todo(fun_code):
    # TODO: obfuscate (look at TODO.md)
    return fun_code

def obfuscate(filename, functions_to_obfuscate=[]):
    with open(filename, 'r') as f:
        code = f.read()

    extracted = 0
    functions = []
    function_codes = []
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise ValueError(f"Invalid Python code: {e}")

    nodes_to_remove = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in functions_to_obfuscate:
            func_code = ast.get_source_segment(code, node)
            function_codes.append(func_code)
            functions.append(node.name)
            nodes_to_remove.append(node)
            extracted += 1

    for node in nodes_to_remove:
        tree.body.remove(node)

    if extracted < len(functions_to_obfuscate):
        raise ValueError(f"Some functions were not found: {set(functions_to_obfuscate) - set(functions)}")

    insert_pos = 0
    for idx, node in enumerate(tree.body):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            insert_pos = idx + 1

    for func_code in function_codes:
        func = todo(func_code)
        func_ast = ast.parse(func)
        tree.body.insert(insert_pos, func_ast.body[0])
        insert_pos += 1

    code = ast.unparse(tree)
    return strip(code)
