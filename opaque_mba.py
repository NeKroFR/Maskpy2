import ast
import random

class OpaquePredicateTransformer(ast.NodeTransformer):
    def __init__(self, encoded_param_names):
        self.encoded_param_names = encoded_param_names

    def generate_single_condition(self):
        # Generate an always-true condition using dummy_int and constants.
        dummy_int = ast.Name(id='dummy_int', ctx=ast.Load())
        zero = ast.Constant(value=0)
        large_const = ast.Constant(value=0xFFFFFFFF)
        rand_const = ast.Constant(value=random.randint(0, 0xFFFFFFFF))

        conditions = [
            # (dummy_int & 0xFFFFFFFF) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.BitAnd(), right=large_const),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int ^ 0) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.BitXor(), right=zero),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int + 0) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.Add(), right=zero),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int - dummy_int) == 0
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.Sub(), right=dummy_int),
                ops=[ast.Eq()],
                comparators=[zero]
            ),
            # (dummy_int | 0) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.BitOr(), right=zero),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int & dummy_int) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.BitAnd(), right=dummy_int),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int * 1) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.Mult(), right=ast.Constant(value=1)),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int << 0) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.LShift(), right=zero),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int >> 0) == dummy_int
            ast.Compare(
                left=ast.BinOp(left=dummy_int, op=ast.RShift(), right=zero),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            ),
            # (dummy_int & rand_const) | (dummy_int & ~rand_const) == dummy_int
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=dummy_int, op=ast.BitAnd(), right=rand_const),
                    op=ast.BitOr(),
                    right=ast.BinOp(left=dummy_int, op=ast.BitAnd(), right=ast.UnaryOp(op=ast.Invert(), operand=rand_const))
                ),
                ops=[ast.Eq()],
                comparators=[dummy_int]
            )
        ]

        return random.choice(conditions)

    def generate_opaque_true(self, depth=0):
        # Generate a complex always-true condition with nested boolean operations.
        if depth > 2 or random.random() < 0.2:
            return self.generate_single_condition()
        op = random.choice([ast.And(), ast.Or()])
        left = self.generate_opaque_true(depth + 1)
        right = self.generate_opaque_true(depth + 1)
        return ast.BoolOp(op=op, values=[left, right])

    def generate_junk_code(self):
        # Generate junk code for the else branch using dummy_int and constants.
        dummy_int = ast.Name(id='dummy_int', ctx=ast.Load())
        rand_const = ast.Constant(value=random.randint(0, 0xFFFFFFFF))
        expr = ast.BinOp(
            left=dummy_int,
            op=random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.BitAnd(), ast.BitOr(), ast.BitXor()]),
            right=rand_const
        )
        return [ast.Assign(targets=[ast.Name(id='dummy', ctx=ast.Store())], value=expr)]

    def visit_If(self, node):
        # Replace if condition with an opaque predicate.
        node.test = self.generate_opaque_true()
        node.body = [self.visit(n) for n in node.body]
        node.orelse = [self.visit(n) for n in node.orelse]
        return node

    def visit_Return(self, node):
        # Wrap return statement with an if-else using an opaque predicate.
        condition = self.generate_opaque_true()
        junk_code = self.generate_junk_code()
        if_stmt = ast.If(test=condition, body=[node], orelse=junk_code)
        return if_stmt

class MBATransformer(ast.NodeTransformer):
    def __init__(self, param_names, param_types):
        self.param_names = [name for name in param_names if param_types.get(name) == 'int']
        self.param_types = param_types

    def is_integer_expr(self, node):
        if isinstance(node, ast.Name):
            return self.param_types.get(node.id) == 'int'
        elif isinstance(node, ast.Constant) and isinstance(node.value, int):
            return True
        return False

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            if self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
                param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
                expr = mba_add(left, right, param, self.param_names)
            else:
                expr = ast.BinOp(left, node.op, right)
        elif isinstance(node.op, ast.Sub):
            if self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
                param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
                expr = mba_sub(left, right, param, self.param_names)
            else:
                expr = ast.BinOp(left, node.op, right)
        else:
            expr = ast.BinOp(left, node.op, right)
        return expr

def mba_add(left, right, param, param_names):
    if param and random.choice([True, False]):
        return ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Add(),
                right=ast.BinOp(
                    left=right,
                    op=ast.Sub(),
                    right=ast.BinOp(
                        left=param,
                        op=ast.BitAnd(),
                        right=ast.UnaryOp(op=ast.Invert(), operand=param)
                    )
                )
            ),
            op=ast.Add(),
            right=ast.BinOp(
                left=param,
                op=ast.BitAnd(),
                right=param
            )
        )
    return ast.BinOp(left=left, op=ast.Add(), right=right)

def mba_sub(left, right, param, param_names):
    if param and random.choice([True, False]):
        return ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Sub(),
                right=ast.BinOp(
                    left=right,
                    op=ast.Add(),
                    right=ast.BinOp(
                        left=param,
                        op=ast.BitOr(),
                        right=ast.UnaryOp(op=ast.Invert(), operand=param)
                    )
                )
            ),
            op=ast.Sub(),
            right=ast.BinOp(
                left=param,
                op=ast.BitOr(),
                right=param
            )
        )
    return ast.BinOp(left=left, op=ast.Sub(), right=right)
