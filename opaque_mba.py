import ast
import random


def _identity_wrap(expr):
    if random.random() > 0.3:
        return expr
    wrapper = random.choice([
        lambda e: ast.BinOp(left=e, op=ast.Add(), right=ast.Constant(value=0)),
        lambda e: ast.BinOp(left=e, op=ast.BitXor(), right=ast.Constant(value=0)),
        lambda e: ast.BinOp(left=e, op=ast.BitOr(), right=ast.Constant(value=0)),
        lambda e: ast.BinOp(left=e, op=ast.Mult(), right=ast.Constant(value=1)),
        lambda e: ast.BinOp(left=ast.Constant(value=0), op=ast.Add(), right=e),
        lambda e: ast.BinOp(left=ast.Constant(value=1), op=ast.Mult(), right=e),
    ])
    return wrapper(expr)


def _maybe_commute(left, op, right):
    if isinstance(op, (ast.Add, ast.Mult, ast.BitAnd, ast.BitOr, ast.BitXor)):
        if random.random() < 0.5:
            return ast.BinOp(left=right, op=op, right=left)
    return ast.BinOp(left=left, op=op, right=right)


class OpaquePredicateTransformer(ast.NodeTransformer):
    def __init__(self, int_param_names, anchor_name='_anc', anchor_value=42):
        self.anchor_name = anchor_name
        self.anchor_value = anchor_value
        self.int_vars = [anchor_name] + list(int_param_names)

    def _var(self, name=None):
        name = name or random.choice(self.int_vars)
        return ast.Name(id=name, ctx=ast.Load())

    def _cmp(self, left, op, right):
        return ast.Compare(left=left, ops=[op], comparators=[right])

    def generate_single_condition(self):
        var = self._var()
        a = random.randint(1, 100)
        mask = random.randint(0, 0xFFFFFFFF)

        conditions = [
            # Number theory: (x * (x + 1)) % 2 == 0
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(
                        left=var, op=ast.Mult(),
                        right=ast.BinOp(left=var, op=ast.Add(), right=ast.Constant(value=1))),
                    op=ast.Mod(), right=ast.Constant(value=2)),
                ast.Eq(), ast.Constant(value=0)),
            # Number theory: (x**2 + x) & 1 == 0
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(
                        left=ast.BinOp(left=var, op=ast.Pow(), right=ast.Constant(value=2)),
                        op=ast.Add(), right=var),
                    op=ast.BitAnd(), right=ast.Constant(value=1)),
                ast.Eq(), ast.Constant(value=0)),
            # Number theory: x**2 % 4 != 3
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(left=var, op=ast.Pow(), right=ast.Constant(value=2)),
                    op=ast.Mod(), right=ast.Constant(value=4)),
                ast.NotEq(), ast.Constant(value=3)),
            # Number theory: (x**3 - x) % 6 == 0 (Fermat)
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(
                        left=ast.BinOp(left=var, op=ast.Pow(), right=ast.Constant(value=3)),
                        op=ast.Sub(), right=var),
                    op=ast.Mod(), right=ast.Constant(value=6)),
                ast.Eq(), ast.Constant(value=0)),
            # Number theory: (x**2 - x) % 2 == 0
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(
                        left=ast.BinOp(left=var, op=ast.Pow(), right=ast.Constant(value=2)),
                        op=ast.Sub(), right=var),
                    op=ast.Mod(), right=ast.Constant(value=2)),
                ast.Eq(), ast.Constant(value=0)),
            # Bitwise: (x | ~x) == -1
            self._cmp(
                ast.BinOp(
                    left=var, op=ast.BitOr(),
                    right=ast.UnaryOp(op=ast.Invert(), operand=var)),
                ast.Eq(), ast.Constant(value=-1)),
            # Algebraic: ((x + a) - a) == x
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(left=var, op=ast.Add(), right=ast.Constant(value=a)),
                    op=ast.Sub(), right=ast.Constant(value=a)),
                ast.Eq(), var),
            # Bitwise identity: ((x & mask) | (~x & mask)) == mask
            self._cmp(
                ast.BinOp(
                    left=ast.BinOp(left=var, op=ast.BitAnd(), right=ast.Constant(value=mask)),
                    op=ast.BitOr(),
                    right=ast.BinOp(
                        left=ast.UnaryOp(op=ast.Invert(), operand=var),
                        op=ast.BitAnd(), right=ast.Constant(value=mask))),
                ast.Eq(), ast.Constant(value=mask)),
            # Idempotent: (x & x) == x
            self._cmp(
                ast.BinOp(left=var, op=ast.BitAnd(), right=var),
                ast.Eq(), var),
            # Idempotent: (x | x) == x
            self._cmp(
                ast.BinOp(left=var, op=ast.BitOr(), right=var),
                ast.Eq(), var),
        ]
        return random.choice(conditions)

    def generate_opaque_true(self, depth=0, max_depth=5):
        if depth >= max_depth or random.random() < 0.3:
            return self.generate_single_condition()
        op = random.choice([ast.And(), ast.Or()])
        count = random.choice([2, 2, 2, 3])
        values = [self.generate_opaque_true(depth + 1, max_depth) for _ in range(count)]
        return ast.BoolOp(op=op, values=values)

    def generate_junk_code(self, max_depth=3):
        if max_depth <= 0:
            return [ast.Pass()]
        dummy = ast.Name(id='_jnk', ctx=ast.Store())
        dummy_load = ast.Name(id='_jnk', ctx=ast.Load())
        var = self._var()
        ops = [ast.Add(), ast.Sub(), ast.Mult(), ast.BitAnd(), ast.BitOr(),
               ast.BitXor(), ast.LShift(), ast.RShift()]
        stmts = [ast.Assign(targets=[dummy], value=ast.Constant(value=0))]
        for _ in range(random.randint(2, 5)):
            op = random.choice(ops)
            val = random.choice([
                ast.Constant(value=random.randint(0, 0xFFFF)),
                ast.BinOp(left=var, op=random.choice(ops),
                           right=ast.Constant(value=random.randint(1, 0xFFF)))
            ])
            stmts.append(ast.Assign(
                targets=[dummy],
                value=ast.BinOp(left=dummy_load, op=op, right=val)))
        if random.random() < 0.5:
            cond = self.generate_opaque_true(depth=2, max_depth=4)
            stmts.append(ast.If(test=cond, body=[ast.Pass()],
                                orelse=self.generate_junk_code(max_depth - 1)))
        return stmts

    def visit_If(self, node):
        # Preserve original condition — wrap entire if in opaque predicate instead
        node.body = [self.visit(n) for n in node.body]
        node.orelse = [self.visit(n) for n in node.orelse] if node.orelse else []
        cond = self.generate_opaque_true(max_depth=5)
        junk = self.generate_junk_code(max_depth=3)
        return ast.If(test=cond, body=[node], orelse=junk)

    def visit_Return(self, node):
        cond = self.generate_opaque_true(max_depth=5)
        junk = self.generate_junk_code(max_depth=3)
        return ast.If(test=cond, body=[node], orelse=junk)


class MBATransformer(ast.NodeTransformer):
    def __init__(self, param_names, param_types, known_int_vars=None):
        self.param_names = [n for n in param_names if param_types.get(n) == 'int']
        self.param_types = param_types
        self.known_int_vars = known_int_vars or set()

    def is_integer_expr(self, node, depth=0):
        if depth > 15:
            return False
        if isinstance(node, ast.Name):
            return self.param_types.get(node.id) == 'int' or node.id in self.known_int_vars
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            return True
        if isinstance(node, ast.BinOp):
            return (self.is_integer_expr(node.left, depth + 1)
                    and self.is_integer_expr(node.right, depth + 1))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.Invert, ast.USub, ast.UAdd)):
            return self.is_integer_expr(node.operand, depth + 1)
        return False

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        is_int = self.is_integer_expr(node.left) and self.is_integer_expr(node.right)
        param = ast.Name(id=random.choice(self.param_names), ctx=ast.Load()) if self.param_names else None

        if is_int:
            if isinstance(node.op, ast.Add):
                return _identity_wrap(mba_add(left, right, param))
            elif isinstance(node.op, ast.Sub):
                return _identity_wrap(mba_sub(left, right, param))
            elif isinstance(node.op, ast.BitXor) and random.random() < 0.5:
                return _identity_wrap(mba_xor(left, right))
            elif isinstance(node.op, ast.BitAnd) and random.random() < 0.5:
                return _identity_wrap(mba_and(left, right))
            elif isinstance(node.op, ast.BitOr) and random.random() < 0.5:
                return _identity_wrap(mba_or(left, right))

        return ast.BinOp(left=left, op=node.op, right=right)


def mba_add(left, right, param=None):
    transforms = [
        # (a ^ b) + 2 * (a & b)
        lambda l, r: _maybe_commute(
            ast.BinOp(left=l, op=ast.BitXor(), right=r),
            ast.Add(),
            ast.BinOp(left=ast.Constant(value=2), op=ast.Mult(),
                       right=ast.BinOp(left=l, op=ast.BitAnd(), right=r))),
        # (a - ~b) - 1
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.Sub(),
                            right=ast.UnaryOp(op=ast.Invert(), operand=r)),
            op=ast.Sub(), right=ast.Constant(value=1)),
        # (a | b) + (a & b)
        lambda l, r: _maybe_commute(
            ast.BinOp(left=l, op=ast.BitOr(), right=r),
            ast.Add(),
            ast.BinOp(left=l, op=ast.BitAnd(), right=r)),
        # 2 * (a | b) - (a ^ b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(
                left=ast.Constant(value=2), op=ast.Mult(),
                right=ast.BinOp(left=l, op=ast.BitOr(), right=r)),
            op=ast.Sub(),
            right=ast.BinOp(left=l, op=ast.BitXor(), right=r)),
        # ((a | b) + (a & b)) + ((a ^ b) - (a | b))
        lambda l, r: ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=l, op=ast.BitOr(), right=r),
                op=ast.Add(),
                right=ast.BinOp(left=l, op=ast.BitAnd(), right=r)),
            op=ast.Add(),
            right=ast.BinOp(
                left=ast.BinOp(left=l, op=ast.BitXor(), right=r),
                op=ast.Sub(),
                right=ast.BinOp(left=l, op=ast.BitOr(), right=r))),
    ]
    if param:
        transforms.append(
            lambda l, r: ast.BinOp(
                left=ast.BinOp(
                    left=ast.BinOp(left=l, op=ast.Add(), right=param),
                    op=ast.BitXor(),
                    right=ast.BinOp(left=r, op=ast.Sub(), right=param)),
                op=ast.Add(),
                right=ast.BinOp(
                    left=ast.Constant(value=2), op=ast.Mult(),
                    right=ast.BinOp(
                        left=ast.BinOp(left=l, op=ast.Add(), right=param),
                        op=ast.BitAnd(),
                        right=ast.BinOp(left=r, op=ast.Sub(), right=param)))))
    return random.choice(transforms)(left, right)


def mba_sub(left, right, param=None):
    transforms = [
        # (a ^ b) - 2 * (b & ~a)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.BitXor(), right=r),
            op=ast.Sub(),
            right=ast.BinOp(
                left=ast.Constant(value=2), op=ast.Mult(),
                right=ast.BinOp(left=r, op=ast.BitAnd(),
                                 right=ast.UnaryOp(op=ast.Invert(), operand=l)))),
        # (a + ~b) + 1
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.Add(),
                            right=ast.UnaryOp(op=ast.Invert(), operand=r)),
            op=ast.Add(), right=ast.Constant(value=1)),
        # ~(~a + b)
        lambda l, r: ast.UnaryOp(
            op=ast.Invert(),
            operand=ast.BinOp(
                left=ast.UnaryOp(op=ast.Invert(), operand=l),
                op=ast.Add(), right=r)),
        # 2*(a & ~b) - (a ^ b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(
                left=ast.Constant(value=2), op=ast.Mult(),
                right=ast.BinOp(left=l, op=ast.BitAnd(),
                                 right=ast.UnaryOp(op=ast.Invert(), operand=r))),
            op=ast.Sub(),
            right=ast.BinOp(left=l, op=ast.BitXor(), right=r)),
        # ((a - b) + (a | b)) - (a | b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(
                left=ast.BinOp(left=l, op=ast.Sub(), right=r),
                op=ast.Add(),
                right=ast.BinOp(left=l, op=ast.BitOr(), right=r)),
            op=ast.Sub(),
            right=ast.BinOp(left=l, op=ast.BitOr(), right=r)),
    ]
    if param:
        transforms.append(
            lambda l, r: ast.BinOp(
                left=ast.BinOp(
                    left=ast.BinOp(left=l, op=ast.Add(), right=param),
                    op=ast.Sub(),
                    right=ast.BinOp(left=r, op=ast.Add(), right=param)),
                op=ast.Add(),
                right=ast.BinOp(left=param, op=ast.BitXor(), right=param)))
    return random.choice(transforms)(left, right)


def mba_xor(left, right):
    transforms = [
        # (a | b) - (a & b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.BitOr(), right=r),
            op=ast.Sub(),
            right=ast.BinOp(left=l, op=ast.BitAnd(), right=r)),
        # (a & ~b) | (~a & b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(
                left=l, op=ast.BitAnd(),
                right=ast.UnaryOp(op=ast.Invert(), operand=r)),
            op=ast.BitOr(),
            right=ast.BinOp(
                left=ast.UnaryOp(op=ast.Invert(), operand=l),
                op=ast.BitAnd(), right=r)),
        # (a | b) & ~(a & b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.BitOr(), right=r),
            op=ast.BitAnd(),
            right=ast.UnaryOp(
                op=ast.Invert(),
                operand=ast.BinOp(left=l, op=ast.BitAnd(), right=r))),
    ]
    return random.choice(transforms)(left, right)


def mba_and(left, right):
    transforms = [
        # ~(~a | ~b) — De Morgan
        lambda l, r: ast.UnaryOp(
            op=ast.Invert(),
            operand=ast.BinOp(
                left=ast.UnaryOp(op=ast.Invert(), operand=l),
                op=ast.BitOr(),
                right=ast.UnaryOp(op=ast.Invert(), operand=r))),
        # (a | b) - (a ^ b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.BitOr(), right=r),
            op=ast.Sub(),
            right=ast.BinOp(left=l, op=ast.BitXor(), right=r)),
    ]
    return random.choice(transforms)(left, right)


def mba_or(left, right):
    transforms = [
        # ~(~a & ~b) — De Morgan
        lambda l, r: ast.UnaryOp(
            op=ast.Invert(),
            operand=ast.BinOp(
                left=ast.UnaryOp(op=ast.Invert(), operand=l),
                op=ast.BitAnd(),
                right=ast.UnaryOp(op=ast.Invert(), operand=r))),
        # (a ^ b) + (a & b)
        lambda l, r: _maybe_commute(
            ast.BinOp(left=l, op=ast.BitXor(), right=r),
            ast.Add(),
            ast.BinOp(left=l, op=ast.BitAnd(), right=r)),
        # (a ^ b) | (a & b)
        lambda l, r: ast.BinOp(
            left=ast.BinOp(left=l, op=ast.BitXor(), right=r),
            op=ast.BitOr(),
            right=ast.BinOp(left=l, op=ast.BitAnd(), right=r)),
    ]
    return random.choice(transforms)(left, right)
