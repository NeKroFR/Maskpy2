import ast
import sys
import random
from strip import strip
from opaque_mba import MBATransformer, OpaquePredicateTransformer
from encode_types import get_type_annotation
from string_encrypt import StringEncryptTransformer, get_string_decrypt_helper
from const_unfold import ConstantUnfolder
from bytecode_obf import encrypt_function
from vm_obf import vm_obfuscate_function

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


def obfuscate_function(fun_code):
    tree = ast.parse(fun_code)
    func_def = tree.body[0]
    param_names = [arg.arg for arg in func_def.args.args]
    param_types = {arg.arg: get_type_annotation(arg.annotation) for arg in func_def.args.args if arg.annotation}

    tree = StringEncryptTransformer().visit(tree)

    tree = MBATransformer(param_names, param_types).visit(tree)
    tree = _break_sharing(tree)
    tree = MBATransformer(param_names, param_types).visit(tree)
    tree = _break_sharing(tree)
    unfolder = ConstantUnfolder(probability=0.6)
    tree = unfolder.visit(tree)

    ast.fix_missing_locations(tree)
    return ast.unparse(tree).strip()


def _encrypt_all_functions(source, vm_func_count=0, vm_count=0):
    tree = ast.parse(source)
    parts = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            func_src = ast.unparse(node)
            # VM compile, fallback to JIT
            if vm_func_count > 0:
                try:
                    vm_src = vm_obfuscate_function(func_src, node.name, vm_count=vm_count)
                    if vm_src:
                        parts.append(vm_src)
                        continue
                except Exception:
                    pass
            try:
                parts.append(encrypt_function(func_src, node.name))
            except SyntaxError:
                parts.append(func_src)
        else:
            parts.append(ast.unparse(node))
    return '\n'.join(parts)


def obfuscate(filename, functions_to_obfuscate=[], vm_count=0):
    with open(filename, 'r') as f:
        code = f.read()

    extracted = 0
    functions = []
    function_codes = []
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise ValueError(f"Invalid Python code: {e}")

    if not functions_to_obfuscate:
        functions_to_obfuscate = [
            node.name for node in tree.body if isinstance(node, ast.FunctionDef)]

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

    tree.body.insert(0, get_string_decrypt_helper())

    insert_pos = 0
    for idx, node in enumerate(tree.body):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            insert_pos = idx + 1

    for i, func_code in enumerate(function_codes):
        func = obfuscate_function(func_code)
        func_ast = ast.parse(func)
        tree.body.insert(insert_pos, func_ast.body[0])
        insert_pos += 1

    code = ast.unparse(tree)
    stripped = strip(code)

    return _encrypt_all_functions(stripped, vm_func_count=len(function_codes), vm_count=vm_count)
