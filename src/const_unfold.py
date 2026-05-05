import ast
import random


class ConstantUnfolder(ast.NodeTransformer):
    def __init__(self, probability=0.7):
        self.probability = probability
        self._depth = 0

    def visit(self, node):
        self._depth += 1
        if self._depth > 200:
            self._depth -= 1
            return node
        result = super().visit(node)
        self._depth -= 1
        return result

    def visit_Constant(self, node):
        if (isinstance(node.value, int)
                and not isinstance(node.value, bool)
                and random.random() < self.probability):
            return self._unfold(node.value)
        return node

    def _unfold(self, n):
        strategies = ['add', 'xor', 'sub', 'mul_add']
        strategy = random.choice(strategies)

        if strategy == 'add':
            a = random.randint(-10000, 10000)
            b = n - a
            return ast.BinOp(
                left=ast.Constant(value=a),
                op=ast.Add(),
                right=ast.Constant(value=b)
            )
        elif strategy == 'xor':
            a = random.randint(0, 0xFFFFFF)
            b = n ^ a
            return ast.BinOp(
                left=ast.Constant(value=a),
                op=ast.BitXor(),
                right=ast.Constant(value=b)
            )
        elif strategy == 'sub':
            b = random.randint(1, 10000)
            a = n + b
            return ast.BinOp(
                left=ast.Constant(value=a),
                op=ast.Sub(),
                right=ast.Constant(value=b)
            )
        elif strategy == 'mul_add':
            d = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
            q = n // d
            r = n - q * d
            mul = ast.BinOp(
                left=ast.Constant(value=q),
                op=ast.Mult(),
                right=ast.Constant(value=d)
            )
            if r == 0:
                return mul
            return ast.BinOp(
                left=mul,
                op=ast.Add(),
                right=ast.Constant(value=r)
            )

        return ast.Constant(value=n)
