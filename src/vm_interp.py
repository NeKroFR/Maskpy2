import random


def generate_interpreter(opcode_table, opcode_defs, chain_seed, xtea_key,
                         siphash_key, constants, names, num_locals, num_args,
                         bytecode, integrity_hash, code_len):
    uid = random.randint(1000, 9999)
    v = {k: f'_{k}{random.randint(10, 99)}' for k in [
        'stk', 'loc', 'pc', 'op', 'code', 'consts', 'names', 'gl',
        'xs', 'tmp', 'a', 'b', 'r', 'iter', 'val',
        'ot', 'cs', 'xs0', 'xs1', 'xs2', 'xs3',
        'h', 'bi', 'v0', 'v1', 'k', 'delta', 's',
        'q1', 'q2', 'q3']}

    fk = [v['q1'], v['q2'], v['q3']]

    lines = []
    _a = lines.append

    # xoshiro256**
    _a(f"def _xn{uid}({v['xs']}):")
    _a(f"    {v['r']} = ((((({v['xs']}[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | (({v['xs']}[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    {v['tmp']} = ({v['xs']}[1] << 17) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    {v['xs']}[2] ^= {v['xs']}[0]")
    _a(f"    {v['xs']}[3] ^= {v['xs']}[1]")
    _a(f"    {v['xs']}[1] ^= {v['xs']}[2]")
    _a(f"    {v['xs']}[0] ^= {v['xs']}[3]")
    _a(f"    {v['xs']}[2] ^= {v['tmp']}")
    _a(f"    {v['xs']}[3] = (({v['xs']}[3] << 45) | ({v['xs']}[3] >> 19)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    return {v['r']}")

    # xtea decrypt
    _a(f"def _xd{uid}({v['v0']}, {v['v1']}, {v['k']}):")
    _a(f"    {v['delta']} = 0x9E3779B9")
    _a(f"    {v['s']} = ({v['delta']} * 32) & 0xFFFFFFFF")
    _a(f"    for _ in range(32):")
    _a(f"        {v['v1']} = ({v['v1']} - (((({v['v0']} << 4) ^ ({v['v0']} >> 5)) + {v['v0']}) ^ ({v['s']} + {v['k']}[({v['s']} >> 11) & 3]))) & 0xFFFFFFFF")
    _a(f"        {v['s']} = ({v['s']} - {v['delta']}) & 0xFFFFFFFF")
    _a(f"        {v['v0']} = ({v['v0']} - (((({v['v1']} << 4) ^ ({v['v1']} >> 5)) + {v['v1']}) ^ ({v['s']} + {v['k']}[{v['s']} & 3]))) & 0xFFFFFFFF")
    _a(f"    return {v['v0']}, {v['v1']}")

    # siphash-2-4
    sv = f'_sv{random.randint(10,99)}'
    _a(f"def _sh{uid}({v['k']}, {v['code']}):")
    _a(f"    {sv} = [int.from_bytes({v['k']}[:8], 'little') ^ 0x736f6d6570736575, int.from_bytes({v['k']}[8:], 'little') ^ 0x646f72616e646f6d, int.from_bytes({v['k']}[:8], 'little') ^ 0x6c7967656e657261, int.from_bytes({v['k']}[8:], 'little') ^ 0x7465646279746573]")
    _a(f"    def _sr():")
    _a(f"        {sv}[0] = ({sv}[0] + {sv}[1]) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[1] = (({sv}[1] << 13) | ({sv}[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[0]")
    _a(f"        {sv}[0] = (({sv}[0] << 32) | ({sv}[0] >> 32)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[2] = ({sv}[2] + {sv}[3]) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[3] = (({sv}[3] << 16) | ({sv}[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[2]")
    _a(f"        {sv}[0] = ({sv}[0] + {sv}[3]) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[3] = (({sv}[3] << 21) | ({sv}[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[0]")
    _a(f"        {sv}[2] = ({sv}[2] + {sv}[1]) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[1] = (({sv}[1] << 17) | ({sv}[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[2]")
    _a(f"        {sv}[2] = (({sv}[2] << 32) | ({sv}[2] >> 32)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    for {v['bi']} in range(0, len({v['code']}) - 7, 8):")
    _a(f"        {v['tmp']} = int.from_bytes({v['code']}[{v['bi']}:{v['bi']}+8], 'little')")
    _a(f"        {sv}[3] ^= {v['tmp']}")
    _a(f"        _sr(); _sr()")
    _a(f"        {sv}[0] ^= {v['tmp']}")
    _a(f"    {v['tmp']} = 0")
    _a(f"    for {v['bi']} in range(len({v['code']}) & ~7, len({v['code']})):")
    _a(f"        {v['tmp']} |= {v['code']}[{v['bi']}] << (8 * ({v['bi']} & 7))")
    _a(f"    {v['tmp']} |= (len({v['code']}) & 0xFF) << 56")
    _a(f"    {sv}[3] ^= {v['tmp']}")
    _a(f"    _sr(); _sr()")
    _a(f"    {sv}[0] ^= {v['tmp']}")
    _a(f"    {sv}[2] ^= 0xFF")
    _a(f"    _sr(); _sr(); _sr(); _sr()")
    _a(f"    return ({sv}[0] ^ {sv}[1] ^ {sv}[2] ^ {sv}[3]) & 0xFFFFFFFFFFFFFFFF")

    # vm entry
    _a(f"def _vm{uid}(*{v['a']}):")

    #
    _a(f"    {v['code']} = bytearray()")
    _a(f"    {v['k']} = {list(xtea_key)}")
    _a(f"    {v['tmp']} = {list(bytecode)}")
    _a(f"    for {v['bi']} in range(0, len({v['tmp']}), 8):")
    _a(f"        {v['v0']} = ({v['tmp']}[{v['bi']}]<<24) | ({v['tmp']}[{v['bi']}+1]<<16) | ({v['tmp']}[{v['bi']}+2]<<8) | {v['tmp']}[{v['bi']}+3]")
    _a(f"        {v['v1']} = ({v['tmp']}[{v['bi']}+4]<<24) | ({v['tmp']}[{v['bi']}+5]<<16) | ({v['tmp']}[{v['bi']}+6]<<8) | {v['tmp']}[{v['bi']}+7]")
    _a(f"        {v['v0']}, {v['v1']} = _xd{uid}({v['v0']}, {v['v1']}, {v['k']})")
    _a(f"        {v['code']}.extend([({v['v0']}>>24)&0xFF, ({v['v0']}>>16)&0xFF, ({v['v0']}>>8)&0xFF, {v['v0']}&0xFF, ({v['v1']}>>24)&0xFF, ({v['v1']}>>16)&0xFF, ({v['v1']}>>8)&0xFF, {v['v1']}&0xFF])")

    #
    _a(f"    {v['code']} = {v['code']}[:{code_len}]")
    _a(f"    if _sh{uid}({bytes(siphash_key)!r}, bytes({v['code']})) != {integrity_hash}: raise {random.choice(['MemoryError', 'RecursionError', 'OSError'])}()")

    #
    _a(f"    {v['cs']} = {list(chain_seed)}")
    _a(f"    for {v['bi']} in range(len({v['code']})):")
    _a(f"        {v['code']}[{v['bi']}] ^= _xn{uid}({v['cs']}) & 0xFF")

    #
    _a(f"    {v['ot']} = {list(opcode_table)}")
    _a(f"    {v['consts']} = {constants!r}")
    _a(f"    {v['names']} = {names!r}")
    _a(f"    {v['gl']} = globals()")
    _a(f"    {v['gl']}.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))")
    _a(f"    {v['stk']} = []")
    _a(f"    {v['loc']} = list({v['a']}[:{num_args}]) + [None] * {num_locals - num_args}")
    _a(f"    {v['pc']} = 0")
    _a(f"    {fk[0]} = len({v['code']}) ^ {random.randint(0, 0xFFFF)}")
    eh = f'_eh{random.randint(10,99)}'
    _a(f"    {eh} = []")  # exception handler stack

    #
    _a(f"    while {v['pc']} < len({v['code']}):")
    _a(f"      try:")

    #
    _a(f"        {v['op']} = {v['ot']}[{v['code']}[{v['pc']}] & 0xFF]")

    #
    first = True
    for op_name, op_val in sorted(opcode_defs.items(), key=lambda x: x[1]):
        kw = 'if' if first else 'elif'
        first = False
        _a(f"        {kw} {v['op']} == {op_val}:")
        if op_name == 'SETUP_EXCEPT':
            _a(f"            {eh}.append(({v['code']}[{v['pc']}+1] | ({v['code']}[{v['pc']}+2] << 8))); {v['pc']} += 3")
        elif op_name == 'POP_EXCEPT':
            _a(f"            {eh}.pop(); {v['pc']} += 1")
        elif op_name == 'MORPH':
            _a(f"            {v['tmp']} = {v['code']}[{v['pc']}+1] | ({v['code']}[{v['pc']}+2] << 8); {v['code']}[{v['tmp']}] ^= {v['code']}[{v['pc']}+3]; {v['pc']} += 4")
        else:
            _gen_handler(lines, v, op_name)

    #
    _a(f"        else: break")
    _a(f"      except Exception as _exc:")
    _a(f"        if {eh}: {v['pc']} = {eh}.pop(); {v['stk']}.append(_exc)")
    _a(f"        else: raise")
    _a(f"    return {v['stk']}[-1] if {v['stk']} else None")

    return '\n'.join(lines), f'_vm{uid}'


def _gen_handler(lines, v, op):
    _a = lines.append
    p = v['pc']
    s = v['stk']
    c = v['code']
    loc = v['loc']
    cn = v['consts']
    nm = v['names']
    gl = v['gl']

    def u8():
        return f"{c}[{p}+1]"
    def u16():
        return f"({c}[{p}+1] | ({c}[{p}+2] << 8))"

    if op == 'PUSH_CONST':
        _a(f"            {s}.append({cn}[{u8()}]); {p} += 2")
    elif op == 'LOAD_LOCAL':
        _a(f"            {s}.append({loc}[{u8()}]); {p} += 2")
    elif op == 'STORE_LOCAL':
        _a(f"            {loc}[{u8()}] = {s}.pop(); {p} += 2")
    elif op == 'LOAD_GLOBAL':
        _a(f"            {s}.append({gl}[{nm}[{u8()}]]); {p} += 2")
    elif op == 'STORE_GLOBAL':
        _a(f"            {gl}[{nm}[{u8()}]] = {s}.pop(); {p} += 2")
    elif op == 'DUP':
        _a(f"            {s}.append({s}[-1]); {p} += 1")
    elif op == 'POP':
        _a(f"            {s}.pop(); {p} += 1")
    elif op == 'ROT2':
        _a(f"            {s}[-1], {s}[-2] = {s}[-2], {s}[-1]; {p} += 1")

    #
    elif op in ('ADD', 'SUB', 'MUL', 'MOD', 'FLOORDIV', 'POW',
                'BITXOR', 'BITAND', 'BITOR', 'LSHIFT', 'RSHIFT'):
        py_op = {
            'ADD': '+', 'SUB': '-', 'MUL': '*', 'MOD': '%',
            'FLOORDIV': '//', 'POW': '**',
            'BITXOR': '^', 'BITAND': '&', 'BITOR': '|',
            'LSHIFT': '<<', 'RSHIFT': '>>',
        }[op]
        _a(f"            {v['b']} = {s}.pop(); {v['a']} = {s}.pop()")
        _a(f"            {s}.append({v['a']} {py_op} {v['b']}); {p} += 1")

    #
    elif op == 'NEG':
        _a(f"            {s}.append(-{s}.pop()); {p} += 1")
    elif op == 'INVERT':
        _a(f"            {s}.append(~{s}.pop()); {p} += 1")
    elif op == 'BOOL_NOT':
        _a(f"            {s}.append(not {s}.pop()); {p} += 1")

    #
    elif op in ('CMP_EQ', 'CMP_NE', 'CMP_LT', 'CMP_GT', 'CMP_LE', 'CMP_GE',
                'CMP_IS', 'CMP_ISNOT', 'CMP_IN'):
        py_op = {
            'CMP_EQ': '==', 'CMP_NE': '!=', 'CMP_LT': '<', 'CMP_GT': '>',
            'CMP_LE': '<=', 'CMP_GE': '>=', 'CMP_IS': 'is', 'CMP_ISNOT': 'is not',
            'CMP_IN': 'in',
        }[op]
        _a(f"            {v['b']} = {s}.pop(); {v['a']} = {s}.pop()")
        _a(f"            {s}.append({v['a']} {py_op} {v['b']}); {p} += 1")

    #
    elif op == 'JMP':
        _a(f"            {p} = {u16()}")
    elif op == 'JT':
        _a(f"            {p} = {u16()} if {s}.pop() else {p} + 3")
    elif op == 'JF':
        _a(f"            {p} = {u16()} if not {s}.pop() else {p} + 3")

    #
    elif op == 'CALL_FUNC':
        _a(f"            {v['tmp']} = {u8()}")
        _a(f"            if {v['tmp']}: {v['val']} = {s}[-{v['tmp']}:]; del {s}[-{v['tmp']}:]")
        _a(f"            else: {v['val']} = []")
        _a(f"            {s}.append({s}.pop()(*{v['val']})); {p} += 2")
    elif op == 'CALL_METHOD':
        _a(f"            {v['tmp']} = {c}[{p}+2]")  # nargs
        _a(f"            {v['val']} = [{s}.pop() for _ in range({v['tmp']})][::-1]")
        _a(f"            {s}.append(getattr({s}.pop(), {nm}[{c}[{p}+1]])(*{v['val']})); {p} += 3")
    elif op == 'LOAD_ATTR':
        _a(f"            {s}.append(getattr({s}.pop(), {nm}[{u8()}])); {p} += 2")
    elif op == 'STORE_ATTR':
        _a(f"            {v['val']} = {s}.pop(); setattr({s}.pop(), {nm}[{u8()}], {v['val']}); {p} += 2")

    #
    elif op == 'BUILD_LIST':
        _a(f"            {v['tmp']} = {u8()}")
        _a(f"            if {v['tmp']}: {v['val']} = {s}[-{v['tmp']}:]; del {s}[-{v['tmp']}:]")
        _a(f"            else: {v['val']} = []")
        _a(f"            {s}.append({v['val']}); {p} += 2")
    elif op == 'BUILD_TUPLE':
        _a(f"            {v['tmp']} = {u8()}")
        _a(f"            if {v['tmp']}: {v['val']} = tuple({s}[-{v['tmp']}:]); del {s}[-{v['tmp']}:]")
        _a(f"            else: {v['val']} = ()")
        _a(f"            {s}.append({v['val']}); {p} += 2")
    elif op == 'BUILD_DICT':
        _a(f"            {v['tmp']} = {u8()}")
        _a(f"            {v['val']} = {{}}")
        _a(f"            for _ in range({v['tmp']}): {v['b']} = {s}.pop(); {v['a']} = {s}.pop(); {v['val']}[{v['a']}] = {v['b']}")
        _a(f"            {s}.append({v['val']}); {p} += 2")
    elif op == 'SUBSCRIPT':
        _a(f"            {v['b']} = {s}.pop(); {v['a']} = {s}.pop()")
        _a(f"            {s}.append({v['a']}[{v['b']}]); {p} += 1")
    elif op == 'STORE_SUBSCRIPT':
        #
        _a(f"            {v['b']} = {s}.pop(); {v['a']} = {s}.pop(); {v['val']} = {s}.pop()")
        _a(f"            {v['a']}[{v['b']}] = {v['val']}; {p} += 1")
    elif op == 'UNPACK':
        _a(f"            {v['val']} = list({s}.pop())[:{u8()}]")
        _a(f"            {s}.extend(reversed({v['val']})); {p} += 2")
    elif op == 'BUILD_SLICE':
        _a(f"            {v['b']} = {s}.pop(); {v['a']} = {s}.pop()")
        _a(f"            {s}.append(slice({v['a']}, {v['b']})); {p} += 1")

    #
    elif op == 'ITER_NEW':
        _a(f"            {s}.append(iter({s}.pop())); {p} += 1")
    elif op == 'ITER_NEXT':
        _a(f"            {v['val']} = next({s}[-1], None)")
        _a(f"            if {v['val']} is None and True:")
        _a(f"                {s}.pop(); {p} = {u16()}")
        _a(f"            else:")
        _a(f"                {s}.append({v['val']}); {p} += 3")

    #
    elif op == 'RET':
        _a(f"            return {s}.pop()")
    elif op == 'HALT':
        _a(f"            return {s}[-1] if {s} else None")


def generate_opcode_table(seed):
    #
    rng = random.Random(seed)
    values = list(range(256))
    rng.shuffle(values)
    return values


def generate_chain_seed(seed):
    #
    def splitmix(s):
        s = (s + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        s = ((s ^ (s >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        s = ((s ^ (s >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        return s ^ (s >> 31)
    state = []
    s = seed
    for _ in range(4):
        s = (s + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        state.append(splitmix(s))
    return state
