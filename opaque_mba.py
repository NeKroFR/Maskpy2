import ast
import random

class OpaquePredicateTransformer(ast.NodeTransformer):
    def __init__(self, encoded_param_names):
        # Include all integer variables
        int_params = [name for name in encoded_param_names if 'int' in name]
        self.int_vars = ['dummy_int'] + int_params

    def generate_single_condition(self):
        """Generate a complex always-true condition."""
        var1 = ast.Name(id=random.choice(self.int_vars), ctx=ast.Load())
        mask = random.randint(0, 0xFFFFFFFF)
        conditions = [
            # (var1 & mask) | (~var1 & mask) == mask
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=var1, op=ast.BitAnd(), right=ast.Constant(value=mask)),
                    op=ast.BitOr(),
                    right=ast.BinOp(left=ast.UnaryOp(op=ast.Invert(), operand=var1), op=ast.BitAnd(), right=ast.Constant(value=mask))
                ),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=mask)]
            ),
            # ((var1 + 3) - 3) == var1
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=var1, op=ast.Add(), right=ast.Constant(value=3)),
                    op=ast.Sub(),
                    right=ast.Constant(value=3)
                ),
                ops=[ast.Eq()],
                comparators=[var1]
            ),
            # (var1 ^ var1) == 0
            ast.Compare(
                left=ast.BinOp(left=var1, op=ast.BitXor(), right=var1),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=0)]
            ),
            # (var1 | (var1 & mask)) == var1
            ast.Compare(
                left=ast.BinOp(
                    left=var1,
                    op=ast.BitOr(),
                    right=ast.BinOp(left=var1, op=ast.BitAnd(), right=ast.Constant(value=mask))
                ),
                ops=[ast.Eq()],
                comparators=[var1]
            ),
            # ((var1 * 2) / 2) == var1
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=var1, op=ast.Mult(), right=ast.Constant(value=2)),
                    op=ast.Div(),
                    right=ast.Constant(value=2)
                ),
                ops=[ast.Eq()],
                comparators=[var1]
            )
        ]
        if len(self.int_vars) >= 2:
            var2 = ast.Name(id=random.choice(self.int_vars), ctx=ast.Load())
            conditions.extend([
                # (var1 + var2 - var2) == var1
                ast.Compare(
                    left=ast.BinOp(
                        left=ast.BinOp(left=var1, op=ast.Add(), right=var2),
                        op=ast.Sub(),
                        right=var2
                    ),
                    ops=[ast.Eq()],
                    comparators=[var1]
                ),
                # ((var1 & var2) ^ (var1 & ~var2)) == var1
                ast.Compare(
                    left=ast.BinOp(
                        left=ast.BinOp(left=var1, op=ast.BitAnd(), right=var2),
                        op=ast.BitXor(),
                        right=ast.BinOp(left=var1, op=ast.BitAnd(), right=ast.UnaryOp(op=ast.Invert(), operand=var2))
                    ),
                    ops=[ast.Eq()],
                    comparators=[var1]
                )
            ])
        return random.choice(conditions)

    def generate_opaque_true(self, depth=0):
        """Generate deeply nested opaque predicates."""
        if depth > 5 or random.random() < 0.25:
            return self.generate_single_condition()
        op = random.choice([ast.And(), ast.Or()])
        left = self.generate_opaque_true(depth + 1)
        right = self.generate_opaque_true(depth + 1)
        if random.random() < 0.3:  # Add extra complexity with a third condition
            extra = self.generate_opaque_true(depth + 1)
            return ast.BoolOp(op=op, values=[left, right, extra])
        return ast.BoolOp(op=op, values=[left, right])

    def generate_junk_code(self):
        """Generate complex, multi-step junk code."""
        dummy = ast.Name(id='dummy', ctx=ast.Store())
        var = ast.Name(id=random.choice(self.int_vars), ctx=ast.Load())
        ops = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.BitAnd(), ast.BitOr(), ast.BitXor()]
        statements = []
        for _ in range(random.randint(3, 5)):  # More steps
            op = random.choice(ops)
            value = random.choice([
                ast.Constant(value=random.randint(0, 0xFFFF)),
                ast.BinOp(left=var, op=random.choice(ops), right=ast.Constant(value=random.randint(0, 0xFF)))
            ])
            expr = ast.BinOp(left=var, op=op, right=value)
            statements.append(ast.Assign(targets=[dummy], value=expr))
            var = dummy
        # Add a fake condition to increase complexity
        fake_cond = self.generate_single_condition()
        statements.append(ast.If(test=fake_cond, body=[ast.Pass()], orelse=[ast.Pass()]))
        return statements

    def visit_If(self, node):
        node.test = self.generate_opaque_true()
        node.body = [self.visit(n) for n in node.body]
        node.orelse = self.generate_junk_code() + [self.visit(n) for n in node.orelse]
        return node

    def visit_Return(self, node):
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
        if isinstance(node.op, ast.Add) and self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
            param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
            expr = mba_add(left, right, param, self.param_names)
        elif isinstance(node.op, ast.Sub) and self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
            param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
            expr = mba_sub(left, right, param, self.param_names)
        else:
            expr = ast.BinOp(left, node.op, right)
        return expr

def mba_add(left, right, param, param_names):
    """Generate highly complex addition transformations."""
    transformations = [
        # (left ^ right) + 2*(left & right)
        ast.BinOp(
            left=ast.BinOp(left=left, op=ast.BitXor(), right=right),
            op=ast.Add(),
            right=ast.BinOp(
                left=ast.Constant(value=2),
                op=ast.Mult(),
                right=ast.BinOp(left=left, op=ast.BitAnd(), right=right)
            )
        ),
        # left - ~right - 1
        ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Sub(),
                right=ast.UnaryOp(op=ast.Invert(), operand=right)
            ),
            op=ast.Sub(),
            right=ast.Constant(value=1)
        ),
        # ((left | right) + (left & right)) + ((left ^ right) - (left | right))
        ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=left, op=ast.BitOr(), right=right),
                op=ast.Add(),
                right=ast.BinOp(left=left, op=ast.BitAnd(), right=right)
            ),
            op=ast.Add(),
            right=ast.BinOp(
                left=ast.BinOp(left=left, op=ast.BitXor(), right=right),
                op=ast.Sub(),
                right=ast.BinOp(left=left, op=ast.BitOr(), right=right)
            )
        )
    ]
    if param:
        # Nested: ((left + param) ^ (right - param)) + 2*((left + param) & (right - param))
        transformations.append(
            ast.BinOp(
                left=ast.BinOp(
                    left=ast.BinOp(left=left, op=ast.Add(), right=param),
                    op=ast.BitXor(),
                    right=ast.BinOp(left=right, op=ast.Sub(), right=param)
                ),
                op=ast.Add(),
                right=ast.BinOp(
                    left=ast.Constant(value=2),
                    op=ast.Mult(),
                    right=ast.BinOp(
                        left=ast.BinOp(left=left, op=ast.Add(), right=param),
                        op=ast.BitAnd(),
                        right=ast.BinOp(left=right, op=ast.Sub(), right=param)
                    )
                )
            )
        )
    return random.choice(transformations)

def mba_sub(left, right, param, param_names):
    """Generate highly complex subtraction transformations."""
    transformations = [
        # (left ^ right) - 2*(right & ~left)
        ast.BinOp(
            left=ast.BinOp(left=left, op=ast.BitXor(), right=right),
            op=ast.Sub(),
            right=ast.BinOp(
                left=ast.Constant(value=2),
                op=ast.Mult(),
                right=ast.BinOp(left=right, op=ast.BitAnd(), right=ast.UnaryOp(op=ast.Invert(), operand=left))
            )
        ),
        # left + ~right + 1
        ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Add(),
                right=ast.UnaryOp(op=ast.Invert(), operand=right)
            ),
            op=ast.Add(),
            right=ast.Constant(value=1)
        ),
        # ((left - right) + (left | right)) - (left | right)
        ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=left, op=ast.Sub(), right=right),
                op=ast.Add(),
                right=ast.BinOp(left=left, op=ast.BitOr(), right=right)
            ),
            op=ast.Sub(),
            right=ast.BinOp(left=left, op=ast.BitOr(), right=right)
        )
    ]
    if param:
        # (left + param) - (right + param)
        transformations.append(
            ast.BinOp(
                left=ast.BinOp(left=left, op=ast.Add(), right=param),
                op=ast.Sub(),
                right=ast.BinOp(left=right, op=ast.Add(), right=param)
            )
        )
    return random.choice(transformations)
