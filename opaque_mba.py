import ast
import random

class OpaquePredicateTransformer(ast.NodeTransformer):
    def __init__(self, encoded_param_names):
        int_params = [name for name in encoded_param_names if 'int' in name]
        self.int_vars = ['dummy_int'] + int_params

    def generate_single_condition(self):
        var1 = ast.Name(id=random.choice(self.int_vars), ctx=ast.Load())
        mask = random.randint(0, 0xFFFFFFFF)
        a = random.randint(1, 10)
        conditions = [
            # (var1 ^ var1) == 0
            ast.Compare(
                left=ast.BinOp(left=var1, op=ast.BitXor(), right=var1),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=0)]
            ),
            # ((var1 + a) - a) == var1
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=var1, op=ast.Add(), right=ast.Constant(value=a)),
                    op=ast.Sub(),
                    right=ast.Constant(value=a)
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
            ),
            # ((var1 & mask) | (~var1 & mask)) == mask
            ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=var1, op=ast.BitAnd(), right=ast.Constant(value=mask)),
                    op=ast.BitOr(),
                    right=ast.BinOp(
                        left=ast.UnaryOp(op=ast.Invert(), operand=var1),
                        op=ast.BitAnd(),
                        right=ast.Constant(value=mask)
                    )
                ),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=mask)]
            )
        ]
        return random.choice(conditions)

    def generate_opaque_true(self, depth=0, max_depth=5):
        if depth >= max_depth or random.random() < 0.3:
            return self.generate_single_condition()
        op = random.choice([ast.And(), ast.Or()])
        values = [self.generate_opaque_true(depth + 1, max_depth), self.generate_opaque_true(depth + 1, max_depth)]
        if random.random() < 0.3:
            values.append(self.generate_opaque_true(depth + 1, max_depth))
        return ast.BoolOp(op=op, values=values)

    def generate_junk_code(self, max_recursion=3):
        if max_recursion <= 0:
            return [ast.Pass()]
        dummy = ast.Name(id='dummy', ctx=ast.Store())
        var = ast.Name(id=random.choice(self.int_vars), ctx=ast.Load())
        ops = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.BitAnd(), ast.BitOr(), ast.BitXor(), ast.LShift(), ast.RShift()]
        statements = [ast.Assign(targets=[dummy], value=ast.Constant(value=0))]
        for _ in range(random.randint(2, 4)):
            op = random.choice(ops)
            value = random.choice([
                ast.Constant(value=random.randint(0, 0xFFFF)),
                ast.BinOp(left=var, op=random.choice(ops), right=ast.Constant(value=random.randint(0, 0xFFF)))
            ])
            expr = ast.BinOp(left=dummy, op=op, right=value)
            statements.append(ast.Assign(targets=[dummy], value=expr))
            var = dummy
        if random.random() < 0.5:
            fake_cond = self.generate_opaque_true(depth=1, max_depth=3)
            statements.append(ast.If(test=fake_cond, body=[ast.Pass()], orelse=self.generate_junk_code(max_recursion - 1)))
        return statements

    def visit_If(self, node):
        node.test = self.generate_opaque_true(max_depth=5)
        node.body = [self.visit(n) for n in node.body]
        node.orelse = self.generate_junk_code(max_recursion=3) + [self.visit(n) for n in node.orelse]
        return node

    def visit_Return(self, node):
        condition = self.generate_opaque_true(max_depth=5)
        junk_code = self.generate_junk_code(max_recursion=3)
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
        param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
        if isinstance(node.op, ast.Add) and self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
            expr = mba_add(left, right, param, self.param_names)
        elif isinstance(node.op, ast.Sub) and self.is_integer_expr(node.left) and self.is_integer_expr(node.right):
            expr = mba_sub(left, right, param, self.param_names)
        else:
            expr = ast.BinOp(left, node.op, right)
        return expr

def mba_add(left, right, param, param_names):
    transformations = [
        ast.BinOp(
            left=ast.BinOp(left=left, op=ast.BitXor(), right=right),
            op=ast.Add(),
            right=ast.BinOp(
                left=ast.Constant(value=2),
                op=ast.Mult(),
                right=ast.BinOp(left=left, op=ast.BitAnd(), right=right)
            )
        ),
        ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Sub(),
                right=ast.UnaryOp(op=ast.Invert(), operand=right)
            ),
            op=ast.Sub(),
            right=ast.Constant(value=1)
        ),
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
        ),
        ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=left, op=ast.LShift(), right=ast.Constant(value=1)),
                op=ast.RShift(),
                right=ast.Constant(value=1)
            ),
            op=ast.Add(),
            right=ast.BinOp(left=left, op=ast.Add(), right=right)
        )
    ]
    if param:
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
    transformations = [
        ast.BinOp(
            left=ast.BinOp(left=left, op=ast.BitXor(), right=right),
            op=ast.Sub(),
            right=ast.BinOp(
                left=ast.Constant(value=2),
                op=ast.Mult(),
                right=ast.BinOp(left=right, op=ast.BitAnd(), right=ast.UnaryOp(op=ast.Invert(), operand=left))
            )
        ),
        ast.BinOp(
            left=ast.BinOp(
                left=left,
                op=ast.Add(),
                right=ast.UnaryOp(op=ast.Invert(), operand=right)
            ),
            op=ast.Add(),
            right=ast.Constant(value=1)
        ),
        ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=left, op=ast.Sub(), right=right),
                op=ast.Add(),
                right=ast.BinOp(left=left, op=ast.BitOr(), right=right)
            ),
            op=ast.Sub(),
            right=ast.BinOp(left=left, op=ast.BitOr(), right=right)
        ),
        ast.BinOp(
            left=ast.BinOp(left=left, op=ast.Sub(), right=right),
            op=ast.Add(),
            right=ast.BinOp(
                left=ast.Constant(value=0),
                op=ast.Sub(),
                right=ast.BinOp(left=right, op=ast.RShift(), right=ast.Constant(value=1))
            )
        )
    ]
    if param:
        transformations.append(
            ast.BinOp(
                left=ast.BinOp(
                    left=ast.BinOp(left=left, op=ast.Add(), right=param),
                    op=ast.Sub(),
                    right=ast.BinOp(left=right, op=ast.Add(), right=param)
                ),
                op=ast.Add(),
                right=ast.BinOp(left=param, op=ast.BitXor(), right=param)
            )
        )
    return random.choice(transformations)