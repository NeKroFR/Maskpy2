import ast
import marshal
import types
import random
import opcode as _opcode

PCG_MULT = 6364136223846793005
K_GOLDEN = 0x9E3779B97F4A7C15
K_SILVER = 0x517CC1B727220A95
K_BRONZE = 0x6A09E667F3BCC908
FNV_OFFSET = 0x811c9dc5
FNV_PRIME = 0x01000193
MASK64 = 0xFFFFFFFFFFFFFFFF
MASK32 = 0xFFFFFFFF


def inject_anti_debug(func_def):
    for method in ('gettrace', 'getprofile'):
        check = ast.If(
            test=ast.Call(
                func=ast.Attribute(
                    value=ast.Call(
                        func=ast.Name(id='__import__', ctx=ast.Load()),
                        args=[ast.Constant(value='sys')],
                        keywords=[]),
                    attr=method, ctx=ast.Load()),
                args=[], keywords=[]),
            body=[ast.Return(value=ast.Constant(value=None))],
            orelse=[])
        func_def.body.insert(0, check)


def encrypt_function(func_source, func_name):
    module_code = compile(func_source, '<_>', 'exec')

    func_code = None
    for const in module_code.co_consts:
        if isinstance(const, types.CodeType):
            func_code = const
            break
    if func_code is None:
        return func_source

    func_code = _inject_dead_recursive(func_code)
    func_code = _strip_code_metadata(func_code)
    marshalled = marshal.dumps(func_code)

    salt = random.randint(0, MASK64)
    n = len(marshalled)
    pcg_seed = (salt * K_GOLDEN + n) & MASK64
    pcg_inc = (salt ^ (n * K_SILVER)) & MASK64
    perm_seed = (pcg_seed ^ pcg_inc ^ K_BRONZE) & MASK64

    # encryption variant
    variant = random.randint(0, 2)

    if variant == 0:
        # pcg xor then permute
        encrypted = _permute(_pcg_xor(marshalled, pcg_seed, pcg_inc), perm_seed)
    elif variant == 1:
        # permute then pcg xor
        encrypted = _pcg_xor(_permute(marshalled, perm_seed), pcg_seed, pcg_inc)
    else:
        # pcg xor only, no permutation
        encrypted = _pcg_xor(marshalled, pcg_seed, pcg_inc)

    return _build_trampoline(func_name, encrypted, salt, variant)


def _strip_code_metadata(code_obj):
    new_consts = []
    for const in code_obj.co_consts:
        if isinstance(const, types.CodeType):
            new_consts.append(_strip_code_metadata(const))
        else:
            new_consts.append(const)
    kwargs = {'co_consts': tuple(new_consts), 'co_filename': '<>', 'co_name': '<>'}
    if hasattr(code_obj, 'co_qualname'):
        kwargs['co_qualname'] = '<>'
    return code_obj.replace(**kwargs)


def _inject_dead_recursive(code_obj):
    new_consts = []
    for const in code_obj.co_consts:
        if isinstance(const, types.CodeType):
            new_consts.append(_inject_dead_recursive(const))
        else:
            new_consts.append(const)
    code_obj = code_obj.replace(co_consts=tuple(new_consts))
    NOP = _opcode.opmap['NOP']
    LOAD_CONST = _opcode.opmap['LOAD_CONST']
    POP_TOP = _opcode.opmap['POP_TOP']
    bytecode = bytearray(code_obj.co_code)
    for _ in range(random.randint(4, 16)):
        if random.random() < 0.5:
            bytecode.extend([NOP, 0])
        else:
            bytecode.extend([LOAD_CONST, 0, POP_TOP, 0])
    return code_obj.replace(co_code=bytes(bytecode))


def _pcg_next(state, inc):
    old = state
    state = (old * PCG_MULT + (inc | 1)) & MASK64
    xorshifted = (((old >> 18) ^ old) >> 27) & MASK32
    rot = (old >> 59) & 0x1F
    val = ((xorshifted >> rot) | (xorshifted << (32 - rot))) & MASK32
    return state, val

def _pcg_xor(data, seed, inc):
    out = bytearray(len(data))
    state = seed
    pos = 0
    while pos < len(data):
        state, val = _pcg_next(state, inc)
        for shift in (0, 8, 16, 24):
            if pos >= len(data):
                break
            out[pos] = data[pos] ^ ((val >> shift) & 0xFF)
            pos += 1
    return bytes(out)

def _permute(data, seed):
    n = len(data)
    perm = list(range(n))
    state = seed
    inc = (seed >> 32) | 1
    for i in range(n - 1, 0, -1):
        state, val = _pcg_next(state, inc)
        j = val % (i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    out = bytearray(n)
    for i in range(n):
        out[perm[i]] = data[i]
    return bytes(out)

def _fnv1a(data):
    h = FNV_OFFSET
    for b in data:
        h = ((h ^ b) * FNV_PRIME) & MASK32
    return h


def _obf_str(s):
    k = random.randint(1, 255)
    enc = [c ^ k for c in s.encode()]
    return f"bytes([c ^ {k} for c in {enc}]).decode()"

def _obf_const64(value):
    a = random.randint(0, MASK64)
    return a, value ^ a

def _obf_const32(value):
    a = random.randint(0, MASK32)
    return a, value ^ a


def _gen_unpermute(v, src, dst):
    return [
        f"    {v['pm']} = list(range({v['n']}))",
        f"    {v['st']} = {v['s3']}",
        f"    {v['ic']} = ({v['s3']} >> 32) | 1",
        f"    for {v['j']} in range({v['n']} - 1, 0, -1):",
        f"        {v['o']} = {v['st']}",
        f"        {v['st']} = ({v['o']} * {v['cm']} + {v['ic']}) & {MASK64}",
        f"        {v['x']} = ((({v['o']} >> 18) ^ {v['o']}) >> 27) & 0xFFFFFFFF",
        f"        {v['r']} = ({v['o']} >> 59) & 0x1F",
        f"        {v['idx']} = (({v['x']} >> {v['r']}) | ({v['x']} << (32 - {v['r']}))) & 0xFFFFFFFF",
        f"        {v['idx']} = {v['idx']} % ({v['j']} + 1)",
        f"        {v['pm']}[{v['j']}], {v['pm']}[{v['idx']}] = {v['pm']}[{v['idx']}], {v['pm']}[{v['j']}]",
        f"    {dst} = bytearray({v['n']})",
        f"    for {v['j']} in range({v['n']}):",
        f"        {dst}[{v['j']}] = {src}[{v['pm']}[{v['j']}]]",
    ]

def _gen_pcg_xor_while(v, src, dst):
    return [
        f"    {dst} = bytearray({v['n']})",
        f"    {v['st']} = {v['s1']}",
        f"    {v['ic']} = {v['s2']} | 1",
        f"    {v['pos']} = 0",
        f"    while {v['pos']} < {v['n']}:",
        f"        {v['o']} = {v['st']}",
        f"        {v['st']} = ({v['o']} * {v['cm']} + {v['ic']}) & {MASK64}",
        f"        {v['x']} = ((({v['o']} >> 18) ^ {v['o']}) >> 27) & 0xFFFFFFFF",
        f"        {v['r']} = ({v['o']} >> 59) & 0x1F",
        f"        {v['val']} = (({v['x']} >> {v['r']}) | ({v['x']} << (32 - {v['r']}))) & 0xFFFFFFFF",
        f"        for {v['sh']} in (0, 8, 16, 24):",
        f"            if {v['pos']} >= {v['n']}: break",
        f"            {dst}[{v['pos']}] = {src}[{v['pos']}] ^ (({v['val']} >> {v['sh']}) & 0xFF)",
        f"            {v['pos']} += 1",
    ]

def _gen_pcg_xor_for(v, src, dst):
    # for-range variant
    return [
        f"    {dst} = bytearray({v['n']})",
        f"    {v['st']} = {v['s1']}",
        f"    {v['ic']} = {v['s2']} | 1",
        f"    for {v['pos']} in range(0, {v['n']}, 4):",
        f"        {v['o']} = {v['st']}",
        f"        {v['st']} = ({v['o']} * {v['cm']} + {v['ic']}) & {MASK64}",
        f"        {v['x']} = ((({v['o']} >> 18) ^ {v['o']}) >> 27) & 0xFFFFFFFF",
        f"        {v['r']} = ({v['o']} >> 59) & 0x1F",
        f"        {v['val']} = (({v['x']} >> {v['r']}) | ({v['x']} << (32 - {v['r']}))) & 0xFFFFFFFF",
        f"        for {v['sh']} in range(min(4, {v['n']} - {v['pos']})):",
        f"            {dst}[{v['pos']} + {v['sh']}] = {src}[{v['pos']} + {v['sh']}] ^ (({v['val']} >> ({v['sh']} * 8)) & 0xFF)",
    ]


def _build_trampoline(func_name, encrypted, salt, variant):
    expected_hash = _fnv1a(encrypted)
    decoy = random.choice(['MemoryError', 'RecursionError', 'RuntimeError', 'OSError'])

    sf1 = random.randint(0, MASK64)
    sf2 = salt ^ sf1

    pcg_a, pcg_b = _obf_const64(PCG_MULT)
    fnv_off_a, fnv_off_b = _obf_const32(FNV_OFFSET)
    fnv_pr_a, fnv_pr_b = _obf_const32(FNV_PRIME)
    kg_a, kg_b = _obf_const64(K_GOLDEN)
    ks_a, ks_b = _obf_const64(K_SILVER)
    kb_a, kb_b = _obf_const64(K_BRONZE)

    str_marshal = _obf_str('marshal')
    str_types = _obf_str('types')
    str_ft = _obf_str('FunctionType')
    str_code = _obf_str('__code__')
    str_def = _obf_str('__defaults__')
    str_kwd = _obf_str('__kwdefaults__')
    str_qn = _obf_str('co_qualname')

    v = {k: f'_{k}{random.randint(10, 99)}' for k in
         ['d', 'sf1', 'sf2', 'salt', 'n', 's1', 's2', 's3',
          'hv', 'bi', 'pm', 'st', 'ic', 'o', 'x', 'r', 'j', 'idx',
          'up', 'out', 'pos', 'val', 'sh', 'co', 'f', 'kw', 'ak',
          'cm', 'fo', 'fp', 'kg', 'ks', 'kb',
          'q1', 'q2', 'q3', 'q4', 'q5']}
    fk = [v['q1'], v['q2'], v['q3'], v['q4'], v['q5']]

    lines = [f"def {func_name}(*_a, **_k):"]

    # anti-debug
    str_sys = _obf_str('sys')
    str_gt = _obf_str('gettrace')
    str_gp = _obf_str('getprofile')
    lines.append(
        f"    if getattr(__import__({str_sys}), {str_gt})() or "
        f"getattr(__import__({str_sys}), {str_gp})(): raise {decoy}()")

    # block 1: loads (shuffled)
    loads = [
        f"    {v['d']} = {encrypted!r}",
        f"    {v['sf1']} = {sf1}",
        f"    {v['sf2']} = {sf2}",
        f"    {v['cm']} = {pcg_a} ^ {pcg_b}",
        f"    {v['fo']} = {fnv_off_a} ^ {fnv_off_b}",
        f"    {v['fp']} = {fnv_pr_a} ^ {fnv_pr_b}",
        f"    {v['kg']} = {kg_a} ^ {kg_b}",
        f"    {v['ks']} = {ks_a} ^ {ks_b}",
        f"    {v['kb']} = {kb_a} ^ {kb_b}",
        f"    {fk[0]} = {random.randint(0, 0xFFFFFF)}",
    ]
    random.shuffle(loads)
    lines.extend(loads)

    # block 2: derive seeds
    lines.extend([
        f"    {v['salt']} = {v['sf1']} ^ {v['sf2']}",
        f"    {v['n']} = len({v['d']})",
        f"    {v['s1']} = ({v['salt']} * {v['kg']} + {v['n']}) & {MASK64}",
        f"    {v['s2']} = ({v['salt']} ^ ({v['n']} * {v['ks']})) & {MASK64}",
        f"    {v['s3']} = ({v['s1']} ^ {v['s2']} ^ {v['kb']}) & {MASK64}",
        f"    {fk[1]} = {v['s1']} & 0xFF",
    ])

    # block 3: integrity hash
    lines.extend([
        f"    {v['hv']} = {v['fo']}",
        f"    for {v['bi']} in {v['d']}:",
        f"        {v['hv']} = (({v['hv']} ^ {v['bi']}) * {v['fp']}) & 0xFFFFFFFF",
        f"    if {v['hv']} != {expected_hash}:",
        f"        {v['d']} = b'\\x00'",
        f"        raise {decoy}()",
    ])

    # pcg loop style
    pcg_gen = random.choice([_gen_pcg_xor_while, _gen_pcg_xor_for])

    # decrypt layers
    if variant == 0:
        # decrypt: unpermute then pcg xor
        lines.extend(_gen_unpermute(v, v['d'], v['up']))
        lines.extend([f"    {fk[2]} = {v['pm']}[0] ^ {fk[1]}"])
        lines.extend(pcg_gen(v, v['up'], v['out']))
        final_var = v['out']
    elif variant == 1:
        # decrypt: pcg xor then unpermute
        lines.extend(pcg_gen(v, v['d'], v['out']))
        lines.extend(_gen_unpermute(v, v['out'], v['up']))
        lines.extend([f"    {fk[2]} = {v['pm']}[0] ^ {fk[1]}"])
        final_var = v['up']
    else:
        # pcg xor only
        lines.extend(pcg_gen(v, v['d'], v['out']))
        lines.extend([f"    {fk[2]} = {fk[1]} ^ {v['n']}"])
        final_var = v['out']

    # unmarshal + wipe + self-patch
    lines.extend([
        f"    _m = __import__({str_marshal})",
        f"    _t = __import__({str_types})",
        f"    {v['co']} = _m.loads(bytes({final_var}))",
        f"    {v['kw']} = {{'co_filename': '<>', 'co_name': '<>'}}",
        f"    if hasattr({v['co']}, {str_qn}): {v['kw']}[{str_qn}] = '<>'",
        f"    {v['co']} = {v['co']}.replace(**{v['kw']})",
        f"    {v['f']} = getattr(_t, {str_ft})({v['co']}, globals())",
        f"    {fk[3]} = {fk[2]} + {fk[0]}",
        f"    {v['d']} = b'\\x00'",
    ])
    if variant in (0, 1):
        lines.append(f"    {v['up']} = b'\\x00'")
    lines.append(f"    {v['out']} = b'\\x00'")

    lines.extend([
        f"    {v['ak']} = {str_code}",
        f"    setattr({func_name}, {v['ak']}, getattr({v['f']}, {v['ak']}))",
        f"    {v['ak']} = {str_def}",
        f"    setattr({func_name}, {v['ak']}, getattr({v['f']}, {v['ak']}))",
        f"    {v['ak']} = {str_kwd}",
        f"    setattr({func_name}, {v['ak']}, getattr({v['f']}, {v['ak']}))",
        f"    {fk[4]} = {fk[3]} ^ len({v['ak']})",
        f"    return {v['f']}(*_a, **_k)",
    ])

    return '\n'.join(lines)
