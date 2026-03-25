import ast
import sys
import random
from strip import strip
from cff import CFFTransformer
from opaque_mba import MBATransformer, OpaquePredicateTransformer
from encode_types import encode_value, decode_value, get_type_annotation, inject_helpers
from string_encrypt import StringEncryptTransformer, get_string_decrypt_helper
from const_unfold import ConstantUnfolder

sys.setrecursionlimit(10000)

def _break_sharing(node):
    if isinstance(node, ast.AST):
        new = type(node)()
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                setattr(new, field, [_break_sharing(item) for item in value])
            elif isinstance(value, ast.AST):
                setattr(new, field, _break_sharing(value))
            else:
                setattr(new, field, value)
        for attr in ('lineno', 'col_offset', 'end_lineno', 'end_col_offset'):
            if hasattr(node, attr):
                setattr(new, attr, getattr(node, attr))
        return new
    return node


def obfuscate_function(fun_code, dbg=False):
    tree = ast.parse(fun_code)
    func_def = tree.body[0]
    param_names = [arg.arg for arg in func_def.args.args]
    param_types = {arg.arg: get_type_annotation(arg.annotation) for arg in func_def.args.args if arg.annotation}

    # Random anchor variable (replaces constant dummy_int = 42)
    anchor_name = f'_a{random.randint(1000, 9999)}'
    anchor_value = random.randint(100, 0xFFFFFF)
    anchor_assign = ast.Assign(
        targets=[ast.Name(id=anchor_name, ctx=ast.Store())],
        value=ast.Constant(value=anchor_value)
    )
    func_def.body.insert(0, anchor_assign)

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

    # String encryption
    string_enc = StringEncryptTransformer()
    tree = string_enc.visit(tree)

    # Opaque Predicate Transformation
    opaque_transformer = OpaquePredicateTransformer(encoded_names, anchor_name, anchor_value)
    tree = opaque_transformer.visit(tree)

    # Mixed Boolean Arithmetic — pass 1
    known_int = {anchor_name}
    mba1 = MBATransformer(param_names, param_types, known_int)
    tree = mba1.visit(tree)

    # Mixed Boolean Arithmetic — pass 2
    mba2 = MBATransformer(param_names, param_types, known_int)
    tree = mba2.visit(tree)

    # Constant unfolding (after MBA, before CFF)
    # Break AST node sharing from MBA to prevent exponential re-visiting
    tree = _break_sharing(tree)
    unfolder = ConstantUnfolder(probability=0.6)
    tree = unfolder.visit(tree)

    # Handle return value decoding (before CFF flattens returns)
    return_type = get_type_annotation(func_def.returns)
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            if (isinstance(node.value, ast.Name) and
                    node.value.id in encoded_names and
                    return_type in ('str', 'bytes')):
                node.value = decode_value(node.value, return_type)

    # Control Flow Flattening
    cff_transformer = CFFTransformer()
    tree = cff_transformer.visit(tree)

    ast.fix_missing_locations(tree)
    return ast.unparse(tree).strip()


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
    tree.body.insert(0, get_string_decrypt_helper())

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
