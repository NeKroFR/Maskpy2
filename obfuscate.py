import ast
import astunparse
from strip import strip
from opaque_mba import MBATransformer, OpaquePredicateTransformer
from cff import CFFTransformer

def obfuscate_function(fun_code, dbg=False):
    """Obfuscate a function using Opaque Predicates, MBA expressions, and Control Flow Flattening."""
    tree = ast.parse(fun_code)
    param_names = [arg.arg for arg in tree.body[0].args.args]
    if dbg:
        print("Original code:")
        print(astunparse.unparse(tree).strip())
        print("\n\n")

    # Opaque Predicate Transformation
    opaque_transformer = OpaquePredicateTransformer(param_names)
    tree = opaque_transformer.visit(tree)
    if dbg:
        print("After opaque predicate transformation:")
        print(astunparse.unparse(tree).strip())
        print("\n\n")

    # Mixed Boolean Arithmetic Transformation
    mba_transformer = MBATransformer(param_names)
    tree = mba_transformer.visit(tree)
    if dbg:
        print("After MBA transformation:")
        print(astunparse.unparse(tree).strip())
        print("\n\n")

    # Control Flow Flattening
    cff_transformer = CFFTransformer()
    tree = cff_transformer.visit(tree)
    if dbg:
        print("After control flow flattening:")
        print(astunparse.unparse(tree).strip())
        print("\n\n")

    ast.fix_missing_locations(tree)
    return astunparse.unparse(tree).strip()

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
        func = obfuscate_function(func_code)
        func_ast = ast.parse(func)
        tree.body.insert(insert_pos, func_ast.body[0])
        insert_pos += 1

    code = ast.unparse(tree)
    return strip(code)
