import ast

def encode_value(value_node):
    if isinstance(value_node, ast.Constant) and isinstance(value_node.value, int):
        return value_node
    elif isinstance(value_node, ast.Constant):
        if isinstance(value_node.value, str):
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Call(
                        func=ast.Name(id='str.encode', ctx=ast.Load()),
                        args=[value_node],
                        keywords=[ast.keyword(arg='encoding', value=ast.Constant(value='utf-8'))]
                    ),
                    attr='__int__',
                    ctx=ast.Load()
                ),
                args=[],
                keywords=[]
            )
        elif isinstance(value_node.value, bytes):
            return ast.Call(
                func=ast.Attribute(
                    value=value_node,
                    attr='__int__',
                    ctx=ast.Load()
                ),
                args=[],
                keywords=[]
            )
    return value_node

def decode_value(encoded_node, original_type):
    if original_type == 'int':
        return encoded_node
    elif original_type == 'str':
        return ast.Call(
            func=ast.Attribute(
                value=ast.Call(
                    func=ast.Name(id='bytes_from_int', ctx=ast.Load()),
                    args=[encoded_node],
                    keywords=[]
                ),
                attr='decode',
                ctx=ast.Load()
            ),
            args=[ast.Constant(value='utf-8')],
            keywords=[]
        )
    elif original_type == 'bytes':
        return ast.Call(
            func=ast.Name(id='bytes_from_int', ctx=ast.Load()),
            args=[encoded_node],
            keywords=[]
        )
    return encoded_node

def get_type_annotation(annotation):
    if isinstance(annotation, ast.Name):
        return annotation.id
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
