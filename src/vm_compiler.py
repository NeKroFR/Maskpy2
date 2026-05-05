import ast
import struct
import random

# opcode definitions
OP = {
    'PUSH_CONST': 0x01, 'LOAD_LOCAL': 0x02, 'STORE_LOCAL': 0x03,
    'LOAD_GLOBAL': 0x04, 'STORE_GLOBAL': 0x05,
    'DUP': 0x06, 'POP': 0x07, 'ROT2': 0x08,

    'ADD': 0x10, 'SUB': 0x11, 'MUL': 0x12, 'MOD': 0x13,
    'FLOORDIV': 0x14, 'POW': 0x15,
    'BITXOR': 0x16, 'BITAND': 0x17, 'BITOR': 0x18,
    'LSHIFT': 0x19, 'RSHIFT': 0x1A,

    'NEG': 0x20, 'INVERT': 0x21, 'BOOL_NOT': 0x22,

    'CMP_EQ': 0x30, 'CMP_NE': 0x31, 'CMP_LT': 0x32,
    'CMP_GT': 0x33, 'CMP_LE': 0x34, 'CMP_GE': 0x35,
    'CMP_IS': 0x36, 'CMP_ISNOT': 0x37, 'CMP_IN': 0x38,

    'JMP': 0x40, 'JT': 0x41, 'JF': 0x42,

    'CALL_FUNC': 0x50, 'LOAD_ATTR': 0x51, 'STORE_ATTR': 0x52,
    'CALL_METHOD': 0x53,
    'BUILD_LIST': 0x54, 'BUILD_TUPLE': 0x55,
    'SUBSCRIPT': 0x56, 'STORE_SUBSCRIPT': 0x57,
    'UNPACK': 0x58, 'BUILD_DICT': 0x59, 'BUILD_SLICE': 0x5A,

    'ITER_NEW': 0x60, 'ITER_NEXT': 0x61,

    'RET': 0x70,
    'SETUP_EXCEPT': 0x78, 'POP_EXCEPT': 0x79,
    'MORPH': 0x7A,

    'HALT': 0xFF,
}

#
_NO_OPERAND = {
    'ADD', 'SUB', 'MUL', 'MOD', 'FLOORDIV', 'POW',
    'BITXOR', 'BITAND', 'BITOR', 'LSHIFT', 'RSHIFT',
    'NEG', 'INVERT', 'BOOL_NOT',
    'CMP_EQ', 'CMP_NE', 'CMP_LT', 'CMP_GT', 'CMP_LE', 'CMP_GE',
    'CMP_IS', 'CMP_ISNOT', 'CMP_IN',
    'DUP', 'POP', 'ROT2', 'RET', 'HALT',
    'SUBSCRIPT', 'STORE_SUBSCRIPT', 'ITER_NEW', 'BUILD_SLICE',
    'POP_EXCEPT',
}
_U8_OPERAND = {
    'PUSH_CONST', 'LOAD_LOCAL', 'STORE_LOCAL', 'LOAD_GLOBAL', 'STORE_GLOBAL',
    'CALL_FUNC', 'LOAD_ATTR', 'STORE_ATTR',
    'BUILD_LIST', 'BUILD_TUPLE', 'UNPACK', 'BUILD_DICT',
}
_U16_OPERAND = {'JMP', 'JT', 'JF', 'ITER_NEXT', 'SETUP_EXCEPT'}
_U8U8_OPERAND = {'CALL_METHOD'}

#
_BINOP_MAP = {
    ast.Add: 'ADD', ast.Sub: 'SUB', ast.Mult: 'MUL', ast.Mod: 'MOD',
    ast.FloorDiv: 'FLOORDIV', ast.Pow: 'POW',
    ast.BitXor: 'BITXOR', ast.BitAnd: 'BITAND', ast.BitOr: 'BITOR',
    ast.LShift: 'LSHIFT', ast.RShift: 'RSHIFT',
}

_UNARYOP_MAP = {
    ast.USub: 'NEG', ast.Invert: 'INVERT', ast.Not: 'BOOL_NOT',
}

_CMPOP_MAP = {
    ast.Eq: 'CMP_EQ', ast.NotEq: 'CMP_NE', ast.Lt: 'CMP_LT',
    ast.Gt: 'CMP_GT', ast.LtE: 'CMP_LE', ast.GtE: 'CMP_GE',
    ast.Is: 'CMP_IS', ast.IsNot: 'CMP_ISNOT', ast.In: 'CMP_IN',
}


def _instr_size(op_name):
    if op_name in _NO_OPERAND:
        return 1
    if op_name in _U8_OPERAND:
        return 2
    if op_name in _U16_OPERAND:
        return 3
    if op_name in _U8U8_OPERAND:
        return 3
    return 1


class CompileResult:
    def __init__(self, code, constants, names, num_locals, num_args, ir=None):
        self.code = code
        self.constants = constants
        self.names = names
        self.num_locals = num_locals
        self.num_args = num_args
        self.ir = ir or []


class VMUnsupported(Exception):
    pass

class VMCompiler(ast.NodeVisitor):
    def __init__(self):
        self.code = []
        self.constants = []
        self.names = []
        self.locals = {}
        self.num_locals = 0
        self.num_args = 0
        self._label_counter = 0
        self._loop_stack = []
        self._globals = set()

    def _reset(self):
        self.code = []
        self.constants = []
        self.names = []
        self.locals = {}
        self.num_locals = 0
        self.num_args = 0
        self._label_counter = 0
        self._loop_stack = []
        self._globals = set()

    def generic_visit(self, node):
        # reject unsupported node types
        unsupported = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                       ast.Lambda, ast.With, ast.Yield, ast.YieldFrom,
                       ast.AsyncFor, ast.AsyncWith, ast.Await,
                       ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
        if isinstance(node, unsupported):
            raise VMUnsupported(type(node).__name__)
        super().generic_visit(node)

    def compile_function(self, func_def):
        self._reset()
        if func_def.args.vararg or func_def.args.kwarg:
            raise VMUnsupported('varargs')
        for arg in func_def.args.args:
            self.add_local(arg.arg)
        self.num_args = len(func_def.args.args)
        for stmt in func_def.body:
            self.visit(stmt)
        # ensure trailing RET
        if not self.code or self.code[-1][0] != 'RET':
            idx = self.add_const(None)
            self.emit('PUSH_CONST', idx)
            self.emit('RET')
        ir = list(self.code)
        result = self._resolve()
        result.ir = ir
        return result

    def emit(self, op, *operands):
        self.code.append((op, *operands))

    def new_label(self):
        self._label_counter += 1
        return f'__L{self._label_counter}'

    def place_label(self, label):
        self.code.append(('LABEL', label))

    def add_const(self, value):
        # reuse existing constant if possible
        for i, c in enumerate(self.constants):
            if c is value or (type(c) == type(value) and c == value):
                return i
        self.constants.append(value)
        return len(self.constants) - 1

    def add_name(self, name):
        if name in self.names:
            return self.names.index(name)
        self.names.append(name)
        return len(self.names) - 1

    def add_local(self, name):
        if name in self.locals:
            return self.locals[name]
        slot = self.num_locals
        self.locals[name] = slot
        self.num_locals += 1
        return slot

    #

    def visit_Constant(self, node):
        idx = self.add_const(node.value)
        self.emit('PUSH_CONST', idx)

    def visit_Global(self, node):
        self._globals.update(node.names)

    def visit_Name(self, node):
        is_global = node.id in self._globals
        if isinstance(node.ctx, ast.Store):
            if is_global:
                idx = self.add_name(node.id)
                self.emit('STORE_GLOBAL', idx)
            elif node.id in self.locals:
                self.emit('STORE_LOCAL', self.locals[node.id])
            else:
                slot = self.add_local(node.id)
                self.emit('STORE_LOCAL', slot)
        elif isinstance(node.ctx, ast.Load):
            if is_global:
                idx = self.add_name(node.id)
                self.emit('LOAD_GLOBAL', idx)
            elif node.id in self.locals:
                self.emit('LOAD_LOCAL', self.locals[node.id])
            else:
                idx = self.add_name(node.id)
                self.emit('LOAD_GLOBAL', idx)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        op_name = _BINOP_MAP.get(type(node.op))
        if op_name is None:
            raise NotImplementedError(f'binop {type(node.op).__name__}')
        self.emit(op_name)

    def visit_UnaryOp(self, node):
        self.visit(node.operand)
        op_name = _UNARYOP_MAP.get(type(node.op))
        if op_name is None:
            raise NotImplementedError(f'unaryop {type(node.op).__name__}')
        self.emit(op_name)

    def visit_Compare(self, node):
        if len(node.ops) == 1:
            self.visit(node.left)
            self.visit(node.comparators[0])
            self.emit(_CMPOP_MAP[type(node.ops[0])])
            return
        # chained comparisons -> short-circuit and
        end_label = self.new_label()
        done_label = self.new_label()
        self.visit(node.left)
        for i, (op, comp) in enumerate(zip(node.ops, node.comparators)):
            self.visit(comp)
            if i < len(node.ops) - 1:
                # need to keep copy of comp for next comparison
                self.emit('DUP')
                self.emit('ROT2')
            self.emit(_CMPOP_MAP[type(op)])
            if i < len(node.ops) - 1:
                self.emit('DUP')
                self.emit('JF', end_label)
                self.emit('POP')
                # the DUP'd comp is now TOS for next iteration as "left"
        self.emit('JMP', done_label)
        self.place_label(end_label)
        # swap out the saved comp value, leave False on stack
        self.emit('ROT2')
        self.emit('POP')
        self.place_label(done_label)

    def visit_BoolOp(self, node):
        end_label = self.new_label()
        for i, val in enumerate(node.values):
            self.visit(val)
            if i < len(node.values) - 1:
                self.emit('DUP')
                if isinstance(node.op, ast.And):
                    self.emit('JF', end_label)
                else:
                    self.emit('JT', end_label)
                self.emit('POP')
        self.place_label(end_label)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            # method call
            self.visit(node.func.value)
            name_idx = self.add_name(node.func.attr)
            for arg in node.args:
                self.visit(arg)
            self.emit('CALL_METHOD', name_idx, len(node.args))
        else:
            self.visit(node.func)
            for arg in node.args:
                self.visit(arg)
            self.emit('CALL_FUNC', len(node.args))

    def visit_Attribute(self, node):
        if isinstance(node.ctx, ast.Load):
            self.visit(node.value)
            idx = self.add_name(node.attr)
            self.emit('LOAD_ATTR', idx)
        elif isinstance(node.ctx, ast.Store):
            idx = self.add_name(node.attr)
            self.emit('STORE_ATTR', idx)

    def visit_Subscript(self, node):
        if isinstance(node.ctx, ast.Load):
            self.visit(node.value)
            if isinstance(node.slice, ast.Slice):
                self._compile_slice(node.slice)
            else:
                self.visit(node.slice)
            self.emit('SUBSCRIPT')
        elif isinstance(node.ctx, ast.Store):
            # store_subscript expects: val obj idx on stack
            # caller should have pushed val already
            self.visit(node.value)
            if isinstance(node.slice, ast.Slice):
                self._compile_slice(node.slice)
            else:
                self.visit(node.slice)
            self.emit('STORE_SUBSCRIPT')

    def _compile_slice(self, node):
        if node.step:
            raise VMUnsupported('slice_step')
        if node.lower:
            self.visit(node.lower)
        else:
            self.emit('PUSH_CONST', self.add_const(None))
        if node.upper:
            self.visit(node.upper)
        else:
            self.emit('PUSH_CONST', self.add_const(None))
        self.emit('BUILD_SLICE')

    def visit_List(self, node):
        for elt in node.elts:
            self.visit(elt)
        self.emit('BUILD_LIST', len(node.elts))

    def visit_Tuple(self, node):
        if isinstance(node.ctx, ast.Load):
            for elt in node.elts:
                self.visit(elt)
            self.emit('BUILD_TUPLE', len(node.elts))

    def visit_Dict(self, node):
        for k, v in zip(node.keys, node.values):
            self.visit(k)
            self.visit(v)
        self.emit('BUILD_DICT', len(node.keys))

    def visit_IfExp(self, node):
        else_label = self.new_label()
        end_label = self.new_label()
        self.visit(node.test)
        self.emit('JF', else_label)
        self.visit(node.body)
        self.emit('JMP', end_label)
        self.place_label(else_label)
        self.visit(node.orelse)
        self.place_label(end_label)

    def visit_JoinedStr(self, node):
        # f-string: compile each part, convert to str, concatenate
        parts = []
        for val in node.values:
            if isinstance(val, ast.Constant):
                self.visit(val)
            elif isinstance(val, ast.FormattedValue):
                self.visit(val.value)
                # call str() on it
                str_idx = self.add_name('str')
                self.emit('LOAD_GLOBAL', str_idx)
                self.emit('ROT2')
                self.emit('CALL_FUNC', 1)
            else:
                self.visit(val)
            parts.append(True)
        # join all parts with add
        for _ in range(len(parts) - 1):
            self.emit('ADD')

    #

    def visit_Assign(self, node):
        self.visit(node.value)
        target = node.targets[0]
        if isinstance(target, ast.Tuple) or isinstance(target, ast.List):
            self.emit('UNPACK', len(target.elts))
            for elt in target.elts:
                self._store_target(elt)
        elif isinstance(target, ast.Subscript):
            # val is on stack, now need obj and idx
            self.visit(target.value)
            self.visit(target.slice)
            self.emit('STORE_SUBSCRIPT')
        elif isinstance(target, ast.Attribute):
            self.visit(target.value)
            idx = self.add_name(target.attr)
            self.emit('STORE_ATTR', idx)
        else:
            self._store_target(target)

    def _store_target(self, target):
        if isinstance(target, ast.Name):
            if target.id in self._globals:
                idx = self.add_name(target.id)
                self.emit('STORE_GLOBAL', idx)
            elif target.id in self.locals:
                self.emit('STORE_LOCAL', self.locals[target.id])
            else:
                slot = self.add_local(target.id)
                self.emit('STORE_LOCAL', slot)
        elif isinstance(target, ast.Subscript):
            self.visit(target.value)
            self.visit(target.slice)
            self.emit('STORE_SUBSCRIPT')
        elif isinstance(target, ast.Attribute):
            self.visit(target.value)
            idx = self.add_name(target.attr)
            self.emit('STORE_ATTR', idx)

    def visit_AugAssign(self, node):
        # load current value
        if isinstance(node.target, ast.Name):
            name = node.target.id
            is_global = name in self._globals
            if is_global:
                idx = self.add_name(name)
                self.emit('LOAD_GLOBAL', idx)
            elif name in self.locals:
                self.emit('LOAD_LOCAL', self.locals[name])
            else:
                self.add_local(name)
                self.emit('LOAD_LOCAL', self.locals[name])
        elif isinstance(node.target, ast.Subscript):
            self.visit(node.target.value)
            self.visit(node.target.slice)
            self.emit('SUBSCRIPT')
        # compile rhs
        self.visit(node.value)
        # emit operation
        op_name = _BINOP_MAP.get(type(node.op))
        if op_name is None:
            raise NotImplementedError(f'augassign op {type(node.op).__name__}')
        self.emit(op_name)
        # store
        if isinstance(node.target, ast.Name):
            name = node.target.id
            if name in self._globals:
                idx = self.add_name(name)
                self.emit('STORE_GLOBAL', idx)
            else:
                self.emit('STORE_LOCAL', self.locals[name])
        elif isinstance(node.target, ast.Subscript):
            self.visit(node.target.value)
            self.visit(node.target.slice)
            self.emit('STORE_SUBSCRIPT')

    def visit_Return(self, node):
        if node.value:
            self.visit(node.value)
        else:
            self.emit('PUSH_CONST', self.add_const(None))
        self.emit('RET')

    def visit_Try(self, node):
        if node.finalbody:
            raise VMUnsupported('try_finally')
        handler_label = self.new_label()
        end_label = self.new_label()
        # set up exception handler
        self.emit('SETUP_EXCEPT', handler_label)
        # compile try body
        for stmt in node.body:
            self.visit(stmt)
        self.emit('POP_EXCEPT')
        self.emit('JMP', end_label)
        # compile except handlers — exception is on TOS when we arrive
        self.place_label(handler_label)
        for i, handler in enumerate(node.handlers):
            next_handler = self.new_label() if i < len(node.handlers) - 1 else None
            if handler.type:
                # isinstance(exc, ExcType) — stack: [..., exc]
                self.emit('DUP')            # [..., exc, exc]
                isinstance_idx = self.add_name('isinstance')
                self.emit('LOAD_GLOBAL', isinstance_idx)  # [..., exc, exc, isinstance]
                self.emit('ROT2')           # [..., exc, isinstance, exc]
                exc_idx = self.add_name(ast.unparse(handler.type))
                self.emit('LOAD_GLOBAL', exc_idx)  # [..., exc, isinstance, exc, ExcType]
                self.emit('CALL_FUNC', 2)   # [..., exc, result]
                if next_handler:
                    self.emit('JF', next_handler)  # pops result, jump if False; stack: [..., exc]
                else:
                    self.emit('POP')  # discard result; stack: [..., exc]
            # stack: [..., exc] — bind or discard
            if handler.name:
                if handler.name in self._globals:
                    idx = self.add_name(handler.name)
                    self.emit('STORE_GLOBAL', idx)
                elif handler.name in self.locals:
                    self.emit('STORE_LOCAL', self.locals[handler.name])
                else:
                    slot = self.add_local(handler.name)
                    self.emit('STORE_LOCAL', slot)
            else:
                self.emit('POP')
            for stmt in handler.body:
                self.visit(stmt)
            self.emit('JMP', end_label)
            if next_handler:
                self.place_label(next_handler)
        self.place_label(end_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)

    def visit_If(self, node):
        else_label = self.new_label()
        end_label = self.new_label()
        self.visit(node.test)
        self.emit('JF', else_label)
        for stmt in node.body:
            self.visit(stmt)
        if node.orelse:
            self.emit('JMP', end_label)
        self.place_label(else_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)
        self.place_label(end_label)

    def visit_While(self, node):
        loop_label = self.new_label()
        end_label = self.new_label()
        self._loop_stack.append((end_label, loop_label))
        self.place_label(loop_label)
        self.visit(node.test)
        self.emit('JF', end_label)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JMP', loop_label)
        self.place_label(end_label)
        self._loop_stack.pop()

    def visit_For(self, node):
        check_label = self.new_label()
        end_label = self.new_label()
        self._loop_stack.append((end_label, check_label))
        self.visit(node.iter)
        self.emit('ITER_NEW')
        self.place_label(check_label)
        self.emit('ITER_NEXT', end_label)
        # store loop variable
        self._store_target(node.target)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JMP', check_label)
        self.place_label(end_label)
        self._loop_stack.pop()

    def visit_Break(self, node):
        if not self._loop_stack:
            raise SyntaxError('break outside loop')
        break_label, _ = self._loop_stack[-1]
        self.emit('JMP', break_label)

    def visit_Continue(self, node):
        if not self._loop_stack:
            raise SyntaxError('continue outside loop')
        _, cont_label = self._loop_stack[-1]
        self.emit('JMP', cont_label)

    def visit_Expr(self, node):
        self.visit(node.value)
        self.emit('POP')

    def visit_Pass(self, node):
        pass

    #

    def _resolve(self):
        # first pass: compute byte offsets, collect label positions
        label_offsets = {}
        offset = 0
        for instr in self.code:
            if instr[0] == 'LABEL':
                label_offsets[instr[1]] = offset
                continue
            op_name = instr[0]
            offset += _instr_size(op_name)
        # second pass: emit bytes
        out = bytearray()
        for instr in self.code:
            if instr[0] == 'LABEL':
                continue
            op_name = instr[0]
            out.append(OP[op_name])
            if op_name in _U8_OPERAND:
                out.append(instr[1] & 0xFF)
            elif op_name in _U16_OPERAND:
                target = instr[1]
                if isinstance(target, str):
                    target = label_offsets[target]
                out.extend(struct.pack('<H', target))
            elif op_name in _U8U8_OPERAND:
                out.append(instr[1] & 0xFF)
                out.append(instr[2] & 0xFF)
        return CompileResult(
            bytes(out), self.constants, self.names,
            self.num_locals, self.num_args,
        )


if __name__ == '__main__':
    # test 1: simple arithmetic
    code1 = 'def f(a: int, b: int) -> int:\n    return a + b'
    tree = ast.parse(code1)
    compiler = VMCompiler()
    result = compiler.compile_function(tree.body[0])
    assert len(result.code) > 0
    assert result.num_args == 2
    print(f'test1: {len(result.code)} bytes, {len(result.constants)} consts')

    # test 2: if/else
    code2 = '''def f(x: int) -> int:
    if x > 0:
        return x
    else:
        return -x'''
    result2 = VMCompiler().compile_function(ast.parse(code2).body[0])
    assert len(result2.code) > 0
    print(f'test2: {len(result2.code)} bytes')

    # test 3: for loop
    code3 = '''def f(n: int) -> int:
    total = 0
    for i in range(n):
        total = total + i
    return total'''
    result3 = VMCompiler().compile_function(ast.parse(code3).body[0])
    assert len(result3.code) > 0
    print(f'test3: {len(result3.code)} bytes')

    # test 4: while + break
    code4 = '''def f(n: int) -> int:
    i = 0
    while True:
        if i >= n:
            break
        i = i + 1
    return i'''
    result4 = VMCompiler().compile_function(ast.parse(code4).body[0])
    assert len(result4.code) > 0
    print(f'test4: {len(result4.code)} bytes')

    # test 5: function call
    code5 = '''def f(a: int, b: int) -> int:
    return max(a, b)'''
    result5 = VMCompiler().compile_function(ast.parse(code5).body[0])
    assert len(result5.code) > 0
    assert 'max' in result5.names
    print(f'test5: {len(result5.code)} bytes')

    # test 6: list + subscript
    code6 = '''def f(a, b, c):
    arr = [a, b, c]
    return arr[1]'''
    result6 = VMCompiler().compile_function(ast.parse(code6).body[0])
    assert len(result6.code) > 0
    print(f'test6: {len(result6.code)} bytes')

    # test 7: tuple unpacking
    code7 = '''def f(a, b):
    a, b = b, a
    return a'''
    result7 = VMCompiler().compile_function(ast.parse(code7).body[0])
    assert len(result7.code) > 0
    print(f'test7: {len(result7.code)} bytes')

    # test 8: method call
    code8 = '''def f(s: str) -> list:
    return s.split(" ")'''
    result8 = VMCompiler().compile_function(ast.parse(code8).body[0])
    assert len(result8.code) > 0
    print(f'test8: {len(result8.code)} bytes')

    # test 9: augmented assign
    code9 = '''def f(n: int) -> int:
    x = 0
    for i in range(n):
        x += i
    return x'''
    result9 = VMCompiler().compile_function(ast.parse(code9).body[0])
    assert len(result9.code) > 0
    print(f'test9: {len(result9.code)} bytes')

    # test 10: dict
    code10 = '''def f():
    d = {"a": 1, "b": 2}
    return d["a"]'''
    result10 = VMCompiler().compile_function(ast.parse(code10).body[0])
    assert len(result10.code) > 0
    print(f'test10: {len(result10.code)} bytes')

    print('all compiler tests passed')
