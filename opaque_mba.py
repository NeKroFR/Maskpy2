import ast
import random

def mba_add(left, right, param=None, param_names=None, depth=0):
    # Transform x + y into a more complex MBA expression with optional nesting.
    if param is None:
        factor = ast.Num(2)
    else:
        factor = ast.BinOp(param, ast.BitOr(), ast.Num(1))
    xor_part = ast.BinOp(left, ast.BitXor(), right)
    and_part = ast.BinOp(left, ast.BitAnd(), right)
    mult_part = ast.BinOp(factor, ast.Mult(), and_part)
    expr = ast.BinOp(xor_part, ast.Add(), mult_part)
    if depth < 2 and random.random() < 0.5 and param_names:
        nested_param = ast.Name(id=random.choice(param_names), ctx=ast.Load())
        expr = mba_add(expr, ast.Num(0), nested_param, param_names, depth + 1)
    return expr

def mba_sub(left, right, param=None, param_names=None, depth=0):
    # Transform x - y into a more complex MBA expression with optional nesting.
    if param is None:
        adjustment = ast.Num(2)
    else:
        adjustment = ast.BinOp(param, ast.BitAnd(), ast.Num(3))
    xor_part = ast.BinOp(left, ast.BitXor(), right)
    not_left = ast.UnaryOp(ast.Invert(), left)
    and_part = ast.BinOp(not_left, ast.BitAnd(), right)
    mult_part = ast.BinOp(adjustment, ast.Mult(), and_part)
    expr = ast.BinOp(xor_part, ast.Sub(), mult_part)
    if depth < 2 and random.random() < 0.5 and param_names:
        nested_param = ast.Name(id=random.choice(param_names), ctx=ast.Load())
        expr = mba_sub(expr, ast.Num(0), nested_param, param_names, depth + 1)
    return expr

class MBATransformer(ast.NodeTransformer):
    def __init__(self, param_names):
        self.param_names = param_names

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
            expr = mba_add(left, right, param, self.param_names)
        elif isinstance(node.op, ast.Sub):
            param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None
            expr = mba_sub(left, right, param, self.param_names)
        else:
            expr = ast.BinOp(left, node.op, right)
        if self.param_names:
            for _ in range(random.randint(2, 5)):
                param1 = ast.Name(id=random.choice(self.param_names), ctx=ast.Load())
                param2 = ast.Name(id=random.choice(self.param_names), ctx=ast.Load())
                complex_zero = ast.BinOp(
                    ast.BinOp(param1, ast.BitAnd(), param2),
                    ast.Mult(),
                    ast.Num(0)
                )
                expr = ast.BinOp(expr, ast.Add(), complex_zero)
        return expr

    def visit_Compare(self, node):
        if len(node.ops) == 1 and isinstance(node.ops[0], (ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq)):
            left = self.visit(node.left)
            right = self.visit(node.comparators[0])
            op = node.ops[0]
            if self.param_names:
                param_name = random.choice(self.param_names)
                param = ast.Name(id=param_name, ctx=ast.Load())
            else:
                param = None
            difference = mba_sub(left, right, param, self.param_names)
            new_compare = ast.Compare(left=difference, ops=[op], comparators=[ast.Num(0)])
            if self.param_names:
                always_true = ast.Compare(
                    left=ast.BinOp(param, ast.Mult(), ast.Num(0)),
                    ops=[ast.Eq()],
                    comparators=[ast.Num(0)]
                )
                combined = ast.BoolOp(op=ast.And(), values=[new_compare, always_true])
                return combined
            return new_compare
        node.left = self.visit(node.left)
        node.comparators = [self.visit(c) for c in node.comparators]
        return node

class OpaquePredicateTransformer(ast.NodeTransformer):
    def __init__(self, param_names):
        self.param_names = param_names

    @staticmethod
    def generate_single_condition(param_names):
        if not param_names:
            constant_conditions = [
                ast.Compare(left=ast.Num(1), ops=[ast.Eq()], comparators=[ast.Num(1)]),
                ast.Compare(left=ast.Num(2), ops=[ast.Gt()], comparators=[ast.Num(1)]),
                ast.Compare(left=ast.BinOp(ast.Num(3), ast.Mult(), ast.Num(0)), ops=[ast.Eq()], comparators=[ast.Num(0)]),
                ast.Compare(left=ast.BinOp(ast.Num(4), ast.Add(), ast.Num(0)), ops=[ast.Eq()], comparators=[ast.Num(4)]),
            ]
            return random.choice(constant_conditions)
        param = ast.Name(id=random.choice(param_names), ctx=ast.Load())
        other_param = ast.Name(id=random.choice(param_names), ctx=ast.Load())
        choice = random.randint(0, 6)
        if choice == 0:
            left = ast.BinOp(param, ast.Mult(), ast.Num(0))
            ops = [ast.Eq()]
            comparators = [ast.Num(0)]
        elif choice == 1:
            left = ast.BinOp(param, ast.Add(), ast.Num(0))
            ops = [ast.Eq()]
            comparators = [param]
        elif choice == 2:
            left = ast.BinOp(param, ast.BitOr(), ast.Num(0))
            ops = [ast.Eq()]
            comparators = [param]
        elif choice == 3:
            left = ast.BinOp(param, ast.BitAnd(), param)
            ops = [ast.Eq()]
            comparators = [param]
        elif choice == 4:
            left = ast.BinOp(param, ast.BitXor(), ast.Num(0))
            ops = [ast.Eq()]
            comparators = [param]
        elif choice == 5:
            left = ast.BinOp(param, ast.BitOr(), other_param)
            ops = [ast.GtE()]
            comparators = [param]
        else:
            left = ast.BinOp(param, ast.BitAnd(), other_param)
            ops = [ast.LtE()]
            comparators = [param]
        return ast.Compare(left=left, ops=ops, comparators=comparators)

    def build_complex_condition(self, conditions, depth=0):
        if len(conditions) == 0:
            return ast.Constant(value=True)
        if len(conditions) == 1 or depth >= 3:
            return conditions[0]
        split_point = random.randint(1, len(conditions) - 1)
        left = self.build_complex_condition(conditions[:split_point], depth + 1)
        right = self.build_complex_condition(conditions[split_point:], depth + 1)
        op = random.choice([ast.And(), ast.Or()])
        return ast.BoolOp(op=op, values=[left, right])

    def generate_opaque_true(self):
        conditions = [self.generate_single_condition(self.param_names) for _ in range(5)]
        combined_condition = self.build_complex_condition(conditions)
        return combined_condition

    def generate_complex_expression(self, depth):
        # Generate a complex expression using binary operations on parameters or constants.
        if depth == 0 or random.random() < 0.2:
            if self.param_names:
                return ast.Name(id=random.choice(self.param_names), ctx=ast.Load())
            else:
                return ast.Num(random.randint(-10, 10))
        op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.BitAnd(), ast.BitOr(), ast.BitXor()])
        left = self.generate_complex_expression(depth - 1)
        right = self.generate_complex_expression(depth - 1)
        return ast.BinOp(left=left, op=op, right=right)

    def generate_junk_code(self):
        # Generate a single return statement with a complex expression.
        expr = self.generate_complex_expression(depth=3)
        return [ast.Return(value=expr)]

    def visit_Return(self, node):
        condition = self.generate_opaque_true()
        junk_code = self.generate_junk_code()
        if_stmt = ast.If(
            test=condition,
            body=[node],
            orelse=junk_code
        )
        return if_stmt
