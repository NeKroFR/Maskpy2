import ast
import astunparse
from strip import strip
from cff import CFFTransformer
from opaque_mba import MBATransformer, OpaquePredicateTransformer
from encode_types import encode_value, decode_value, get_type_annotation, inject_helpers

def obfuscate_function(fun_code, dbg=False):
    tree = ast.parse(fun_code)
    func_def = tree.body[0]
    param_names = [arg.arg for arg in func_def.args.args]
    param_types = {arg.arg: get_type_annotation(arg.annotation) for arg in func_def.args.args if arg.annotation}

    # Add dummy integer
    dummy_int_assign = ast.Assign(
        targets=[ast.Name(id='dummy_int', ctx=ast.Store())],
        value=ast.Constant(value=42)
    )
    func_def.body.insert(0, dummy_int_assign)

    # Encode parameters
    encoded_assigns = []
    encoded_names = []
    for arg in func_def.args.args:
        param_name = arg.arg
        encoded_name = f"encoded_{param_name}"
        encoded_names.append(encoded_name)
        encoded_value = encode_value(ast.Name(id=param_name, ctx=ast.Load()))
        encoded_assigns.append(
            ast.Assign(
                targets=[ast.Name(id=encoded_name, ctx=ast.Store())],
                value=encoded_value
            )
        )
    func_def.body = encoded_assigns + func_def.body

    # Opaque Predicate Transformation
    opaque_transformer = OpaquePredicateTransformer(encoded_names)
    tree = opaque_transformer.visit(tree)

    # Mixed Boolean Arithmetic Transformation
    mba_transformer = MBATransformer(param_names, param_types)
    tree = mba_transformer.visit(tree)
    
    # Control Flow Flattening
    cff_transformer = CFFTransformer()
    tree = cff_transformer.visit(tree)

    # Handle return value decoding
    return_type = get_type_annotation(func_def.returns)
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            if (isinstance(node.value, ast.Name) and 
                node.value.id in encoded_names and 
                return_type in ('str', 'bytes')):
                node.value = decode_value(node.value, return_type)

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

    # Inject helper functions
    tree = inject_helpers(tree)

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
