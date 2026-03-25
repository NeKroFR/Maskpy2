import ast

def encode_value(name_node, param_type, xor_key=0):
    if param_type == 'int':
        # param ^ xor_key
        return ast.BinOp(
            left=name_node, op=ast.BitXor(),
            right=ast.Constant(value=xor_key))
    elif param_type == 'float':
        # int(param * 2**52)
        return ast.Call(
            func=ast.Name(id='int', ctx=ast.Load()),
            args=[ast.BinOp(
                left=name_node, op=ast.Mult(),
                right=ast.Constant(value=2**52))],
            keywords=[])
    elif param_type == 'str':
        # int.from_bytes(param.encode('utf-8'), 'big')
        return ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='int', ctx=ast.Load()),
                attr='from_bytes', ctx=ast.Load()),
            args=[
                ast.Call(
                    func=ast.Attribute(
                        value=name_node, attr='encode', ctx=ast.Load()),
                    args=[ast.Constant(value='utf-8')],
                    keywords=[]),
                ast.Constant(value='big')
            ],
            keywords=[])
    elif param_type == 'bytes':
        # int.from_bytes(param, 'big')
        return ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='int', ctx=ast.Load()),
                attr='from_bytes', ctx=ast.Load()),
            args=[name_node, ast.Constant(value='big')],
            keywords=[])
    elif param_type == 'bool':
        # int(param) ^ xor_key
        return ast.BinOp(
            left=ast.Call(
                func=ast.Name(id='int', ctx=ast.Load()),
                args=[name_node], keywords=[]),
            op=ast.BitXor(),
            right=ast.Constant(value=xor_key))
    elif param_type in ('list', 'tuple', 'dict', 'set'):
        # len(param) — int anchor, no round-trip
        return ast.Call(
            func=ast.Name(id='len', ctx=ast.Load()),
            args=[name_node], keywords=[])
    # no annotation or unknown type
    return name_node

def decode_value(encoded_node, original_type, xor_key=0):
    if original_type == 'int':
        return ast.BinOp(
            left=encoded_node, op=ast.BitXor(),
            right=ast.Constant(value=xor_key))
    elif original_type == 'float':
        # encoded / 2**52
        return ast.BinOp(
            left=encoded_node, op=ast.Div(),
            right=ast.Constant(value=2**52))
    elif original_type == 'str':
        return ast.Call(
            func=ast.Attribute(
                value=ast.Call(
                    func=ast.Name(id='bytes_from_int', ctx=ast.Load()),
                    args=[encoded_node], keywords=[]),
                attr='decode', ctx=ast.Load()),
            args=[ast.Constant(value='utf-8')],
            keywords=[])
    elif original_type == 'bytes':
        return ast.Call(
            func=ast.Name(id='bytes_from_int', ctx=ast.Load()),
            args=[encoded_node], keywords=[])
    elif original_type == 'bool':
        return ast.Call(
            func=ast.Name(id='bool', ctx=ast.Load()),
            args=[ast.BinOp(
                left=encoded_node, op=ast.BitXor(),
                right=ast.Constant(value=xor_key))],
            keywords=[])
    return encoded_node

def get_type_annotation(annotation):
    if isinstance(annotation, ast.Name):
        return annotation.id
    if isinstance(annotation, ast.Attribute):
        return annotation.attr
    if isinstance(annotation, ast.Subscript):
        if isinstance(annotation.value, ast.Name):
            return annotation.value.id
    return None

helper_code = """
def bytes_from_int(n):
    if n == 0:
        return b'\\x00'
    bytes_result = bytearray()
    while n:
        bytes_result.append(n & 0xFF)
        n >>= 8
    return bytes(bytes_result[::-1])
"""

def inject_helpers(tree):
    helper_ast = ast.parse(helper_code.strip())
    tree.body = helper_ast.body + tree.body
    return tree
