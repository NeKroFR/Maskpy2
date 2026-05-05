import ast
import random

DECRYPT_FUNC = '_sd'


class StringEncryptTransformer(ast.NodeTransformer):
    def __init__(self):
        self.has_strings = False
        self._in_fstring = False

    def visit_JoinedStr(self, node):
        old = self._in_fstring
        self._in_fstring = True
        self.generic_visit(node)
        self._in_fstring = old
        return node

    def visit_Constant(self, node):
        if self._in_fstring:
            return node
        if isinstance(node.value, str) and len(node.value) > 0:
            self.has_strings = True
            return self._encrypt_string(node.value)
        if isinstance(node.value, bytes) and len(node.value) > 0:
            self.has_strings = True
            return self._encrypt_bytes(node.value)
        return node

    def _encrypt_string(self, s):
        data = s.encode('utf-8')
        key = bytes([random.randint(1, 255) for _ in range(len(data))])
        encrypted = bytes([d ^ k for d, k in zip(data, key)])
        return ast.Call(
            func=ast.Attribute(
                value=ast.Call(
                    func=ast.Name(id=DECRYPT_FUNC, ctx=ast.Load()),
                    args=[ast.Constant(value=encrypted), ast.Constant(value=key)],
                    keywords=[]
                ),
                attr='decode',
                ctx=ast.Load()
            ),
            args=[ast.Constant(value='utf-8')],
            keywords=[]
        )

    def _encrypt_bytes(self, b):
        key = bytes([random.randint(1, 255) for _ in range(len(b))])
        encrypted = bytes([d ^ k for d, k in zip(b, key)])
        return ast.Call(
            func=ast.Name(id=DECRYPT_FUNC, ctx=ast.Load()),
            args=[ast.Constant(value=encrypted), ast.Constant(value=key)],
            keywords=[]
        )


def get_string_decrypt_helper():
    code = f"def {DECRYPT_FUNC}(d, k):\n    return bytes([a ^ b for a, b in zip(d, k)])"
    return ast.parse(code).body[0]
