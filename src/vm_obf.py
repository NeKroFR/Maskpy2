import ast
import random
import struct

# ops that can be withheld from static dispatch and injected at runtime
_SAFE_TO_WITHHOLD = {
    'PUSH_CONST', 'LOAD_LOCAL', 'STORE_LOCAL', 'LOAD_GLOBAL', 'STORE_GLOBAL',
    'DUP', 'POP', 'ROT2',
    'ADD', 'SUB', 'MUL',
    'BITXOR', 'BITAND', 'BITOR', 'LSHIFT', 'RSHIFT',
    'NEG', 'INVERT', 'BOOL_NOT',
    'CMP_EQ', 'CMP_NE', 'CMP_LT', 'CMP_GT', 'CMP_LE', 'CMP_GE',
    'CMP_IS', 'CMP_ISNOT', 'CMP_IN',
    'BUILD_LIST', 'BUILD_TUPLE', 'BUILD_DICT',
    'UNPACK', 'BUILD_SLICE',
    'ITER_NEW',
    'REG_LOAD', 'REG_STORE', 'REG_PUSH', 'REG_POP',
    'REG_MOV', 'REG_ADD', 'REG_SUB',
    'XFER_PUSH_SHARED', 'XFER_POP_SHARED', 'XFER_STORE_GREG', 'XFER_LOAD_GREG',
    'LOAD_ADD', 'LOAD_SUB', 'PUSH_STORE', 'LOAD2', 'DUP_STORE', 'LOAD_CMP',
    'NOP',
}


def vm_obfuscate_function(func_source, func_name, vm_count=0):
    from vm_compiler import VMCompiler, OP, _NO_OPERAND, _U8_OPERAND, _U16_OPERAND, _U8U8_OPERAND
    from vm_crypto import (xoshiro256_init, xoshiro256_next, xtea_encrypt_bytes,
                           siphash, derive_vm_key, MASK64)
    from vm_interp import (generate_interpreter, generate_opcode_table,
                           generate_chain_seed)
    from vm_splitter import split_instructions
    from vm_compound import fuse_opcodes

    tree = ast.parse(func_source)
    func_def = tree.body[0]
    compiler = VMCompiler()
    result = compiler.compile_function(func_def)

    if result is None or len(result.code) == 0:
        return None

    master_seed = random.randint(0, MASK64)
    siphash_key = bytes(random.randint(0, 255) for _ in range(16))

    # try/except can't span VMs
    has_try = any(instr[0] in ('SETUP_EXCEPT', 'POP_EXCEPT') for instr in result.ir)
    n_vms = 1 if has_try else (vm_count if vm_count >= 2 else random.randint(3, 5))
    rng = random.Random(master_seed)

    split = split_instructions(result.ir, n_vms, rng)
    n_vms = len(split.segments)

    vm_data = []
    all_ops = dict(OP)
    from vm_isa import XFER_OPS, REG_OPS, POLY_OPS
    all_ops.update(XFER_OPS)
    all_ops.update(REG_OPS)
    all_ops.update(POLY_OPS)

    from vm_isa import generate_compound_set
    compounds = generate_compound_set(rng, count=2)
    for cname, cinfo in compounds.items():
        all_ops[cname] = cinfo['byte']

    for vm_id in range(n_vms):
        segment_ir = split.segments[vm_id]
        if not segment_ir:
            segment_ir = [('HALT',)]

        segment_ir = fuse_opcodes(segment_ir, compounds, rng)
        if rng.random() < 0.4:
            segment_ir = _insert_nop_padding(segment_ir, rng)
        segment_ir = _insert_morph_preamble(segment_ir, rng)
        used = set(instr[0] for instr in segment_ir if instr[0] != 'LABEL')

        bytecode = _resolve_segment(segment_ir, all_ops, _NO_OPERAND, _U8_OPERAND, _U16_OPERAND, _U8U8_OPERAND)

        perm_seed = master_seed ^ (vm_id * 0x9E3779B9)
        opcode_table = generate_opcode_table(perm_seed)
        inverse_table = [0] * 256
        for i, logical in enumerate(opcode_table):
            inverse_table[logical] = i
        permuted_bytecode = _apply_permutation(bytecode, segment_ir, all_ops,
                                                inverse_table, _NO_OPERAND, _U8_OPERAND, _U16_OPERAND, _U8U8_OPERAND)
        permuted_bytecode = _apply_morph_corruption(permuted_bytecode, segment_ir, all_ops,
                                                     _NO_OPERAND, _U8_OPERAND, _U16_OPERAND, _U8U8_OPERAND)

        chain_seed = generate_chain_seed(master_seed ^ (vm_id * 0x1337CAFE))
        encrypted_code = _chain_encrypt(permuted_bytecode, chain_seed[:])
        xtea_key = derive_vm_key(master_seed, siphash_key, vm_id)
        integrity = siphash(siphash_key, encrypted_code)
        xtea_encrypted = xtea_encrypt_bytes(encrypted_code, xtea_key)

        vm_data.append({
            'vm_id': vm_id,
            'opcode_table': opcode_table,
            'chain_seed': chain_seed,
            'xtea_key': xtea_key,
            'bytecode': list(xtea_encrypted),
            'integrity': integrity,
            'code_len': len(encrypted_code),
            'used_ops': used,
        })

    seg_instr_counts = []
    for vm_id, _ in split.dispatch_order:
        seg = split.segments[vm_id]
        count = sum(1 for instr in seg if instr[0] not in ('LABEL', 'VM_YIELD'))
        seg_instr_counts.append(count)

    interp_src, vm_name = _generate_multi_interp(
        vm_data=vm_data,
        opcode_defs=all_ops,
        siphash_key=siphash_key,
        constants=result.constants,
        names=result.names,
        num_locals=result.num_locals,
        num_args=result.num_args,
        dispatch_order=split.dispatch_order,
        n_shared_stacks=split.n_shared_stacks,
        n_global_regs=split.n_global_regs,
        seg_instr_counts=seg_instr_counts,
    )

    func_ast = ast.parse(func_source)
    func_def = func_ast.body[0]
    defaults = [ast.unparse(d) for d in func_def.args.defaults]
    num_required = result.num_args - len(defaults)

    if defaults:
        defs_tuple = '(' + ', '.join(defaults) + ',)'
        wrapper = (
            f"{interp_src}\n"
            f"def {func_name}(*_args, **_kwargs):\n"
            f"    _defs = {defs_tuple}\n"
            f"    _full = list(_args)\n"
            f"    if len(_full) < {result.num_args}:\n"
            f"        _full.extend(_defs[len(_full) - {num_required}:])\n"
            f"    return {vm_name}(*_full)\n"
        )
    else:
        wrapper = (
            f"{interp_src}\n"
            f"def {func_name}(*_args, **_kwargs):\n"
            f"    return {vm_name}(*_args)\n"
        )
    return wrapper


def _resolve_segment(ir, op_map, no_op, u8_op, u16_op, u8u8_op):
    xfer_no = {'VM_YIELD', 'HALT', 'NOP', 'POP_EXCEPT'}
    xfer_u8 = {'XFER_PUSH_SHARED', 'XFER_POP_SHARED', 'XFER_STORE_GREG', 'XFER_LOAD_GREG',
                'REG_PUSH', 'REG_POP',
                'LOAD_ADD', 'LOAD_SUB', 'DUP_STORE', 'LOAD_CMP'}
    xfer_u16 = {'SETUP_EXCEPT'}
    reg_u8u8 = {'REG_LOAD', 'REG_STORE', 'REG_MOV', 'REG_ADD', 'REG_SUB',
                 'PUSH_STORE', 'LOAD2'}

    label_offsets = {}
    offset = 0
    for instr in ir:
        if instr[0] == 'LABEL':
            label_offsets[instr[1]] = offset
            continue
        op = instr[0]
        if op == 'MORPH':
            offset += 4  # opcode + u16 target + u8 mask
        elif op in no_op or op in xfer_no:
            offset += 1
        elif op in u8_op or op in xfer_u8:
            offset += 2
        elif op in u16_op or op in xfer_u16:
            offset += 3
        elif op in u8u8_op or op in reg_u8u8:
            offset += 3
        else:
            offset += 1

    out = bytearray()
    for instr in ir:
        if instr[0] == 'LABEL':
            continue
        op = instr[0]
        if op not in op_map:
            continue
        out.append(op_map[op])
        if op == 'MORPH':
            target = instr[1]
            if isinstance(target, str):
                target = label_offsets.get(target, 0)
            out.extend(struct.pack('<H', target))
            out.append(instr[2] & 0xFF)  # mask
        elif op in u8_op or op in xfer_u8:
            out.append(instr[1] & 0xFF)
        elif op in u16_op or op in xfer_u16:
            target = instr[1]
            if isinstance(target, str):
                target = label_offsets.get(target, 0)
            out.extend(struct.pack('<H', target))
        elif op in u8u8_op or op in reg_u8u8:
            out.append(instr[1] & 0xFF)
            out.append(instr[2] & 0xFF)

    return bytes(out)


def _apply_permutation(bytecode, ir, op_map, inverse_table, no_op, u8_op, u16_op, u8u8_op):
    xfer_no = {'VM_YIELD', 'HALT', 'POP_EXCEPT'}
    xfer_u8 = {'XFER_PUSH_SHARED', 'XFER_POP_SHARED', 'XFER_STORE_GREG', 'XFER_LOAD_GREG',
                'REG_PUSH', 'REG_POP',
                'LOAD_ADD', 'LOAD_SUB', 'DUP_STORE', 'LOAD_CMP'}
    xfer_u16 = {'SETUP_EXCEPT'}
    reg_u8u8 = {'REG_LOAD', 'REG_STORE', 'REG_MOV', 'REG_ADD', 'REG_SUB',
                 'PUSH_STORE', 'LOAD2'}

    out = bytearray(bytecode)
    pos = 0
    for instr in ir:
        if instr[0] == 'LABEL':
            continue
        op = instr[0]
        if op not in op_map or pos >= len(out):
            continue
        # permute the opcode byte
        out[pos] = inverse_table[out[pos]] & 0xFF
        if op == 'MORPH':
            pos += 4
        elif op in no_op or op in xfer_no:
            pos += 1
        elif op in u8_op or op in xfer_u8:
            pos += 2
        elif op in u16_op or op in xfer_u16:
            pos += 3
        elif op in u8u8_op or op in reg_u8u8:
            pos += 3
        else:
            pos += 1
    return bytes(out)


def _insert_morph_preamble(ir, rng):
    """Prepend MORPH instructions that XOR-corrupt later opcode bytes."""
    candidates = []
    for i, instr in enumerate(ir):
        if instr[0] not in ('LABEL', 'MORPH', 'HALT', 'VM_YIELD', 'NOP',
                             'SETUP_EXCEPT', 'POP_EXCEPT'):
            candidates.append(i)
    half = len(candidates) // 2
    if half < 2:
        return ir
    targets = candidates[half:]
    n_morphs = min(rng.randint(2, 4), len(targets))
    chosen = rng.sample(targets, n_morphs)

    morph_preamble = []
    new_ir = list(ir)
    offset = 0
    for idx, target_pos in enumerate(sorted(chosen)):
        label = f'_morph_t{idx}'
        mask = rng.randint(1, 255)
        new_ir.insert(target_pos + offset, ('LABEL', label))
        offset += 1
        morph_preamble.append(('MORPH', label, mask))
    return morph_preamble + new_ir


def _apply_morph_corruption(bytecode, ir, op_map, no_op, u8_op, u16_op, u8u8_op):
    """Pre-XOR MORPH target bytes so runtime MORPH restores them."""
    xfer_no = {'VM_YIELD', 'HALT', 'NOP', 'POP_EXCEPT'}
    xfer_u8 = {'XFER_PUSH_SHARED', 'XFER_POP_SHARED', 'XFER_STORE_GREG', 'XFER_LOAD_GREG',
                'REG_PUSH', 'REG_POP', 'LOAD_ADD', 'LOAD_SUB', 'DUP_STORE', 'LOAD_CMP'}
    xfer_u16 = {'SETUP_EXCEPT'}
    reg_u8u8 = {'REG_LOAD', 'REG_STORE', 'REG_MOV', 'REG_ADD', 'REG_SUB',
                 'PUSH_STORE', 'LOAD2'}

    out = bytearray(bytecode)
    pos = 0
    for instr in ir:
        if instr[0] == 'LABEL':
            continue
        op = instr[0]
        if op not in op_map:
            continue
        if op == 'MORPH':
            target = out[pos + 1] | (out[pos + 2] << 8)
            mask = out[pos + 3]
            if target < len(out):
                out[target] ^= mask
            pos += 4
        elif op in no_op or op in xfer_no:
            pos += 1
        elif op in u8_op or op in xfer_u8:
            pos += 2
        elif op in u16_op or op in xfer_u16:
            pos += 3
        elif op in u8u8_op or op in reg_u8u8:
            pos += 3
        else:
            pos += 1
    return bytes(out)


def _insert_nop_padding(ir, rng):
    safe_after = {'STORE_LOCAL', 'STORE_GLOBAL', 'POP', 'ADD', 'SUB', 'MUL',
                  'MOD', 'FLOORDIV', 'POW', 'BITXOR', 'BITAND', 'BITOR',
                  'NEG', 'INVERT', 'BOOL_NOT', 'CMP_EQ', 'CMP_NE', 'CMP_LT',
                  'CMP_GT', 'CMP_LE', 'CMP_GE', 'DUP', 'SUBSCRIPT',
                  'NOP', 'VM_YIELD'}
    out = []
    for instr in ir:
        out.append(instr)
        if instr[0] in safe_after and rng.random() < 0.15:
            n_nops = rng.randint(1, 2)
            for _ in range(n_nops):
                out.append(('NOP',))
    return out


def _chain_encrypt(code, chain_state):
    from vm_crypto import xoshiro256_next
    out = bytearray(len(code))
    state = list(chain_state)
    for i in range(len(code)):
        keystream = xoshiro256_next(state)
        out[i] = code[i] ^ (keystream & 0xFF)
    return bytes(out)


def _select_withheld_ops(opcode_defs, used_ops, fraction=0.3):
    candidates = [op for op in opcode_defs if op in _SAFE_TO_WITHHOLD and op in used_ops]
    if not candidates:
        return set()
    count = max(1, int(len(candidates) * fraction))
    withheld = set(random.sample(candidates, min(count, len(candidates))))
    decoys = [op for op in opcode_defs if op in _SAFE_TO_WITHHOLD
              and op not in used_ops and op not in withheld]
    if decoys:
        withheld.update(random.sample(decoys, min(2, len(decoys))))
    return withheld


def _make_dynamic_handler(op_name, func_name):
    """Generate handler function source. Returns new pc."""
    u8 = "d[p+1]"
    sig = f"def {func_name}(s,l,c,n,g,d,p,r,h,x):\n"

    arith = {'ADD':'+','SUB':'-','MUL':'*','MOD':'%','FLOORDIV':'//','POW':'**',
             'BITXOR':'^','BITAND':'&','BITOR':'|','LSHIFT':'<<','RSHIFT':'>>'}
    if op_name in arith:
        return sig + f" b=s.pop();a=s.pop();s.append(a{arith[op_name]}b);return p+1"

    cmps = {'CMP_EQ':'==','CMP_NE':'!=','CMP_LT':'<','CMP_GT':'>','CMP_LE':'<=','CMP_GE':'>=',
            'CMP_IS':' is ','CMP_ISNOT':' is not ','CMP_IN':' in '}
    if op_name in cmps:
        return sig + f" b=s.pop();a=s.pop();s.append(a{cmps[op_name]}b);return p+1"

    simple = {
        'PUSH_CONST': f" s.append(c[{u8}]);return p+2",
        'LOAD_LOCAL': f" s.append(l[{u8}]);return p+2",
        'STORE_LOCAL': f" l[{u8}]=s.pop();return p+2",
        'LOAD_GLOBAL': f" s.append(g[n[{u8}]]);return p+2",
        'STORE_GLOBAL': f" g[n[{u8}]]=s.pop();return p+2",
        'DUP': " s.append(s[-1]);return p+1",
        'POP': " s.pop();return p+1",
        'ROT2': " s[-1],s[-2]=s[-2],s[-1];return p+1",
        'NEG': " s.append(-s.pop());return p+1",
        'INVERT': " s.append(~s.pop());return p+1",
        'BOOL_NOT': " s.append(not s.pop());return p+1",
        'SUBSCRIPT': " b=s.pop();a=s.pop();s.append(a[b]);return p+1",
        'STORE_SUBSCRIPT': " b=s.pop();a=s.pop();v=s.pop();a[b]=v;return p+1",
        'BUILD_SLICE': " b=s.pop();a=s.pop();s.append(slice(a,b));return p+1",
        'LOAD_ATTR': f" s.append(getattr(s.pop(),n[{u8}]));return p+2",
        'STORE_ATTR': f" v=s.pop();setattr(s.pop(),n[{u8}],v);return p+2",
        'UNPACK': f" v=list(s.pop())[:{u8}];s.extend(reversed(v));return p+2",
        'ITER_NEW': " s.append(iter(s.pop()));return p+1",
        'NOP': " return p+1",
        'REG_LOAD': " r[d[p+1]]=l[d[p+2]];return p+3",
        'REG_STORE': " l[d[p+2]]=r[d[p+1]];return p+3",
        'REG_PUSH': f" s.append(r[{u8}]);return p+2",
        'REG_POP': f" r[{u8}]=s.pop();return p+2",
        'REG_MOV': " r[d[p+1]]=r[d[p+2]];return p+3",
        'REG_ADD': " r[d[p+1]]=r[d[p+1]]+r[d[p+2]];return p+3",
        'REG_SUB': " r[d[p+1]]=r[d[p+1]]-r[d[p+2]];return p+3",
        'XFER_PUSH_SHARED': f" h[{u8}].append(s.pop());return p+2",
        'XFER_POP_SHARED': f" s.append(h[{u8}].pop());return p+2",
        'XFER_STORE_GREG': f" x[{u8}]=s.pop();return p+2",
        'XFER_LOAD_GREG': f" s.append(x[{u8}]);return p+2",
        'LOAD_ADD': f" s.append(l[{u8}]);b=s.pop();a=s.pop();s.append(a+b);return p+2",
        'LOAD_SUB': f" s.append(l[{u8}]);b=s.pop();a=s.pop();s.append(a-b);return p+2",
        'PUSH_STORE': " l[d[p+2]]=c[d[p+1]];return p+3",
        'LOAD2': " s.append(l[d[p+1]]);s.append(l[d[p+2]]);return p+3",
        'DUP_STORE': f" s.append(s[-1]);l[{u8}]=s.pop();return p+2",
        'LOAD_CMP': f" s.append(l[{u8}]);b=s.pop();a=s.pop();s.append(a<b);return p+2",
    }
    body = simple.get(op_name)
    if body is not None:
        return sig + body

    # multi-line (control flow)
    if op_name == 'BUILD_LIST':
        return sig + f" t={u8}\n if t:v=s[-t:];del s[-t:]\n else:v=[]\n s.append(v);return p+2"
    if op_name == 'BUILD_TUPLE':
        return sig + f" t={u8}\n if t:v=tuple(s[-t:]);del s[-t:]\n else:v=()\n s.append(v);return p+2"
    if op_name == 'BUILD_DICT':
        return sig + f" t={u8};v=" + "{}\n for _ in range(t):b=s.pop();a=s.pop();v[a]=b\n s.append(v);return p+2"

    return None


def _generate_multi_interp(vm_data, opcode_defs, siphash_key, constants, names,
                            num_locals, num_args, dispatch_order,
                            n_shared_stacks, n_global_regs, seg_instr_counts=None):
    uid = random.randint(1000, 9999)
    n_vms = len(vm_data)

    v = {k: f'_{k}{random.randint(10, 99)}' for k in [
        'a', 'b', 'val', 'tmp', 'bi', 'v0', 'v1', 'k', 'delta', 's',
        'op', 'sh', 'co', 'f', 'pc', 'code', 'stk', 'loc', 'consts',
        'names', 'gl', 'ot', 'cs', 'seg', 'seg_vm', 'seg_n', 'r',
        'shared', 'gregs', 'codes', 'pcs', 'stks', 'ots',
        'q1', 'q2']}

    lines = []
    _a = lines.append

    # xoshiro256**
    _a(f"def _xn{uid}({v['cs']}):")
    _a(f"    {v['r']} = ((((({v['cs']}[1] * 5) & 0xFFFFFFFFFFFFFFFF) << 7 | (({v['cs']}[1] * 5) & 0xFFFFFFFFFFFFFFFF) >> 57) & 0xFFFFFFFFFFFFFFFF) * 9) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    {v['tmp']} = ({v['cs']}[1] << 17) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    {v['cs']}[2] ^= {v['cs']}[0]; {v['cs']}[3] ^= {v['cs']}[1]; {v['cs']}[1] ^= {v['cs']}[2]; {v['cs']}[0] ^= {v['cs']}[3]")
    _a(f"    {v['cs']}[2] ^= {v['tmp']}; {v['cs']}[3] = (({v['cs']}[3] << 45) | ({v['cs']}[3] >> 19)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    return {v['r']}")

    # xtea decrypt
    _a(f"def _xd{uid}({v['v0']}, {v['v1']}, {v['k']}):")
    _a(f"    {v['delta']} = 0x9E3779B9; {v['s']} = ({v['delta']} * 32) & 0xFFFFFFFF")
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
    _a(f"        {sv}[0] = ({sv}[0] + {sv}[1]) & 0xFFFFFFFFFFFFFFFF; {sv}[1] = (({sv}[1] << 13) | ({sv}[1] >> 51)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[0]; {sv}[0] = (({sv}[0] << 32) | ({sv}[0] >> 32)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"        {sv}[2] = ({sv}[2] + {sv}[3]) & 0xFFFFFFFFFFFFFFFF; {sv}[3] = (({sv}[3] << 16) | ({sv}[3] >> 48)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[2]")
    _a(f"        {sv}[0] = ({sv}[0] + {sv}[3]) & 0xFFFFFFFFFFFFFFFF; {sv}[3] = (({sv}[3] << 21) | ({sv}[3] >> 43)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[0]")
    _a(f"        {sv}[2] = ({sv}[2] + {sv}[1]) & 0xFFFFFFFFFFFFFFFF; {sv}[1] = (({sv}[1] << 17) | ({sv}[1] >> 47)) & 0xFFFFFFFFFFFFFFFF ^ {sv}[2]; {sv}[2] = (({sv}[2] << 32) | ({sv}[2] >> 32)) & 0xFFFFFFFFFFFFFFFF")
    _a(f"    for {v['bi']} in range(0, len({v['code']}) - 7, 8):")
    _a(f"        {v['tmp']} = int.from_bytes({v['code']}[{v['bi']}:{v['bi']}+8], 'little'); {sv}[3] ^= {v['tmp']}; _sr(); _sr(); {sv}[0] ^= {v['tmp']}")
    _a(f"    {v['tmp']} = 0")
    _a(f"    for {v['bi']} in range(len({v['code']}) & ~7, len({v['code']})): {v['tmp']} |= {v['code']}[{v['bi']}] << (8 * ({v['bi']} & 7))")
    _a(f"    {v['tmp']} |= (len({v['code']}) & 0xFF) << 56; {sv}[3] ^= {v['tmp']}; _sr(); _sr(); {sv}[0] ^= {v['tmp']}; {sv}[2] ^= 0xFF; _sr(); _sr(); _sr(); _sr()")
    _a(f"    return ({sv}[0] ^ {sv}[1] ^ {sv}[2] ^ {sv}[3]) & 0xFFFFFFFFFFFFFFFF")

    # vm entry
    _a(f"def _vm{uid}(*{v['a']}):")

    # spaghetti init (real + decoy VMs interleaved)
    n_decoys = random.randint(1, 2)
    init_blocks = []

    for i, vd in enumerate(vm_data):
        block = []
        block.append(f"    _c{i} = bytearray()")
        block.append(f"    _ek{i} = {vd['xtea_key']!r}")
        block.append(f"    _ed{i} = {vd['bytecode']}")
        block.append(f"    for {v['bi']} in range(0, len(_ed{i}), 8):")
        block.append(f"        {v['v0']} = (_ed{i}[{v['bi']}]<<24)|(_ed{i}[{v['bi']}+1]<<16)|(_ed{i}[{v['bi']}+2]<<8)|_ed{i}[{v['bi']}+3]")
        block.append(f"        {v['v1']} = (_ed{i}[{v['bi']}+4]<<24)|(_ed{i}[{v['bi']}+5]<<16)|(_ed{i}[{v['bi']}+6]<<8)|_ed{i}[{v['bi']}+7]")
        block.append(f"        {v['v0']},{v['v1']} = _xd{uid}({v['v0']},{v['v1']},_ek{i})")
        block.append(f"        _c{i}.extend([({v['v0']}>>24)&0xFF,({v['v0']}>>16)&0xFF,({v['v0']}>>8)&0xFF,{v['v0']}&0xFF,({v['v1']}>>24)&0xFF,({v['v1']}>>16)&0xFF,({v['v1']}>>8)&0xFF,{v['v1']}&0xFF])")
        block.append(f"    _c{i} = _c{i}[:{vd['code_len']}]")
        block.append(f"    if _sh{uid}({siphash_key!r}, bytes(_c{i})) != {vd['integrity']}: raise MemoryError()")
        block.append(f"    _cs{i} = {vd['chain_seed']!r}")
        block.append(f"    for {v['bi']} in range(len(_c{i})): _c{i}[{v['bi']}] ^= _xn{uid}(_cs{i}) & 0xFF")
        init_blocks.append((True, block))

    # decoy VMs
    for d in range(n_decoys):
        fake_id = n_vms + d
        fake_len = random.choice([8, 16, 24])
        fake_data = bytes(random.randint(0, 255) for _ in range(fake_len))
        fake_key = tuple(random.randint(0, 0xFFFFFFFF) for _ in range(4))
        block = []
        block.append(f"    _c{fake_id} = bytearray()")
        block.append(f"    _ek{fake_id} = {fake_key!r}")
        block.append(f"    _ed{fake_id} = {list(fake_data)}")
        block.append(f"    for {v['bi']} in range(0, len(_ed{fake_id}), 8):")
        block.append(f"        {v['v0']} = (_ed{fake_id}[{v['bi']}]<<24)|(_ed{fake_id}[{v['bi']}+1]<<16)|(_ed{fake_id}[{v['bi']}+2]<<8)|_ed{fake_id}[{v['bi']}+3]")
        block.append(f"        {v['v1']} = (_ed{fake_id}[{v['bi']}+4]<<24)|(_ed{fake_id}[{v['bi']}+5]<<16)|(_ed{fake_id}[{v['bi']}+6]<<8)|_ed{fake_id}[{v['bi']}+7]")
        block.append(f"        {v['v0']},{v['v1']} = _xd{uid}({v['v0']},{v['v1']},_ek{fake_id})")
        block.append(f"        _c{fake_id}.extend([({v['v0']}>>24)&0xFF,({v['v0']}>>16)&0xFF,({v['v0']}>>8)&0xFF,{v['v0']}&0xFF,({v['v1']}>>24)&0xFF,({v['v1']}>>16)&0xFF,({v['v1']}>>8)&0xFF,{v['v1']}&0xFF])")
        init_blocks.append((False, block))

    random.shuffle(init_blocks)
    for _, block in init_blocks:
        lines.extend(block)

    _a(f"    {v['shared']} = [[] for _ in range({n_shared_stacks})]")
    _a(f"    {v['gregs']} = [None] * {n_global_regs}")
    _a(f"    {v['loc']} = list({v['a']}[:{num_args}]) + [None] * {num_locals - num_args}")
    _a(f"    {v['consts']} = {constants!r}")
    _a(f"    {v['names']} = {names!r}")
    _a(f"    {v['gl']} = globals()")
    _a(f"    {v['gl']}.update(__builtins__ if isinstance(__builtins__, dict) else vars(__builtins__))")

    # dynamic preamble: withheld ops
    vm_withheld = []
    vm_static_ops = []
    for i in range(n_vms):
        withheld = _select_withheld_ops(opcode_defs, vm_data[i].get('used_ops', set()))
        vm_withheld.append(withheld)
        vm_static_ops.append({k: val for k, val in opcode_defs.items() if k not in withheld})

    # per-VM init + dynamic handler preamble
    for i in range(n_vms):
        _a(f"    _ot{i} = {list(vm_data[i]['opcode_table'])}")
        _a(f"    _stk{i} = []")
        _a(f"    _pc{i} = 0")
        _a(f"    _regs{i} = [None] * 8")
        _a(f"    _eh{i} = []")

        # encrypted handler preamble
        if vm_withheld[i]:
            handler_code = ""
            handler_map = {}
            for idx, op_name in enumerate(sorted(vm_withheld[i])):
                fname = f'_hf{i}_{idx}'
                hcode = _make_dynamic_handler(op_name, fname)
                if hcode is None:
                    continue
                handler_code += hcode + '\n'
                handler_map[op_name] = (fname, opcode_defs[op_name])
            if handler_code:
                xor_key = random.randint(1, 255)
                encrypted = [b ^ xor_key for b in handler_code.encode()]
                ns_var = f'_ns{i}'
                _a(f"    {ns_var} = {{}}")
                _a(f"    exec(bytes(b^{xor_key} for b in {encrypted}).decode(),{ns_var})")
                dh_entries = ', '.join(f"{oval}: {ns_var}['{fname}']"
                                       for fname, oval in handler_map.values())
                _a(f"    _dh{i} = {{{dh_entries}}}")
            else:
                _a(f"    _dh{i} = {{}}")
        else:
            _a(f"    _dh{i} = {{}}")

    # timing + canaries
    tc = f'_tc{random.randint(10, 99)}'
    _a(f"    {tc} = __import__('time').perf_counter_ns")
    _a(f"    _segs = {dispatch_order!r}")
    _a(f"    _tprev = {tc}()")

    #
    canary_var = f'_ck{random.randint(10, 99)}'
    if seg_instr_counts:
        _a(f"    {canary_var} = {seg_instr_counts!r}")
    else:
        _a(f"    {canary_var} = []")
    seg_idx_var = f'_si{random.randint(10, 99)}'
    _a(f"    {seg_idx_var} = 0")

    _a(f"    for {v['seg_vm']}, {v['seg_n']} in _segs:")

    #
    td = f'_td{random.randint(10, 99)}'
    _a(f"        {td} = {tc}() - _tprev")
    _a(f"        if {td} > 5000000000: return None")
    _a(f"        _tprev = {tc}()")

    # polymorphic dispatch (4 styles)
    dispatch_styles = [random.choice(['elif', 'dict', 'array', 'tree']) for _ in range(n_vms)]

    for i in range(n_vms):
        ic = f'_ic{i}'
        kw = 'if' if i == 0 else 'elif'
        _a(f"        {kw} {v['seg_vm']} == {i}:")
        _a(f"            {ic} = 0")
        _a(f"            while _pc{i} < len(_c{i}):")
        _a(f"              try:")
        _a(f"                {ic} += 1")
        _a(f"                {v['op']} = _ot{i}[_c{i}[_pc{i}] & 0xFF]")

        # dynamic handler check
        if vm_withheld[i]:
            _a(f"                if {v['op']} in _dh{i}:")
            _a(f"                    _pc{i} = _dh{i}[{v['op']}](_stk{i}, {v['loc']}, {v['consts']}, {v['names']}, {v['gl']}, _c{i}, _pc{i}, _regs{i}, {v['shared']}, {v['gregs']})")
            _a(f"                    continue")

        # static dispatch
        args = (lines, v, f'_c{i}', f'_stk{i}', f'_pc{i}', f'_regs{i}',
                v['loc'], v['consts'], v['names'], v['gl'],
                v['shared'], v['gregs'], vm_static_ops[i], uid)
        style = dispatch_styles[i]
        if style == 'dict':
            _emit_dict_dispatch(*args, i)
        elif style == 'array':
            _emit_array_dispatch(*args, i)
        elif style == 'tree':
            _emit_tree_dispatch(*args, i)
        else:
            _emit_handlers(*args)

        #
        _a(f"              except Exception as _exc:")
        _a(f"                if _eh{i}: _pc{i} = _eh{i}.pop(); _stk{i}.append(_exc)")
        _a(f"                else: raise")

    # cross-VM heartbeat
    hb = f'_hb{random.randint(10, 99)}'
    hb_prev = f'_hp{random.randint(10, 99)}'
    hb_mults = [random.randint(1, 255) for _ in range(n_vms + 1)]
    _a(f"        {hb} = 0")
    for i in range(n_vms):
        _a(f"        {hb} = ({hb} + len(_stk{i}) * {hb_mults[i]}) & 0xFFFF")
    _a(f"        {hb} = ({hb} + _pc0 * {hb_mults[-1]}) & 0xFFFF")
    #
    _a(f"        if len({v['loc']}) != {num_locals}: return None")
    _a(f"        {seg_idx_var} += 1")

    _a(f"    return _stk0[-1] if _stk0 else None")

    return '\n'.join(lines), f'_vm{uid}'


def _emit_array_dispatch(lines, v, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, op_defs, uid, vm_idx):
    """Array-indexed dispatch variant."""
    _a = lines.append
    arr = f'_ha{vm_idx}{random.randint(10,99)}'
    hi = f'_ai{vm_idx}{random.randint(10,99)}'
    sorted_ops = sorted(op_defs.items(), key=lambda x: x[1])
    #
    mapping = [255] * 256
    for idx, (_, op_val) in enumerate(sorted_ops):
        mapping[op_val] = idx
    _a(f"                {arr} = {mapping}")
    _a(f"                {hi} = {arr}[{v['op']}]")
    first = True
    for handler_idx, (op_name, _) in enumerate(sorted_ops):
        kw = 'if' if first else 'elif'
        first = False
        _a(f"                {kw} {hi} == {handler_idx}:")
        _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid)
    _a(f"                else: {pc} += 1")


def _emit_tree_dispatch(lines, v, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, op_defs, uid, vm_idx):
    """Binary search tree dispatch variant."""
    _a = lines.append
    sorted_ops = sorted(op_defs.items(), key=lambda x: x[1])

    def emit_tree(ops, indent):
        hi = indent + '    '  # handler indent (one level deeper)
        if not ops:
            _a(f"{indent}{pc} += 1")
            return
        if len(ops) == 1:
            op_name, op_val = ops[0]
            _a(f"{indent}if {v['op']} == {op_val}:")
            _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid, indent=hi)
            _a(f"{indent}else: {pc} += 1")
            return
        mid = len(ops) // 2
        mid_val = ops[mid][1]
        _a(f"{indent}if {v['op']} < {mid_val}:")
        # left subtree
        left = [o for o in ops[:mid]]
        if len(left) == 1:
            op_name, op_val = left[0]
            _a(f"{hi}if {v['op']} == {op_val}:")
            _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid, indent=hi + '    ')
            _a(f"{hi}else: {pc} += 1")
        elif left:
            emit_tree(left, hi)
        else:
            _a(f"{hi}{pc} += 1")
        # right subtree (>= mid_val)
        _a(f"{indent}else:")
        right = ops[mid:]
        if len(right) == 1:
            op_name, op_val = right[0]
            _a(f"{hi}if {v['op']} == {op_val}:")
            _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid, indent=hi + '    ')
            _a(f"{hi}else: {pc} += 1")
        else:
            emit_tree(right, hi)

    emit_tree(sorted_ops, '                ')


def _emit_dict_dispatch(lines, v, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, op_defs, uid, vm_idx):
    """Dict-based dispatch variant."""
    _a = lines.append
    #
    dt = f'_dt{vm_idx}{random.randint(10,99)}'
    hi = f'_hi{vm_idx}{random.randint(10,99)}'

    #
    sorted_ops = sorted(op_defs.items(), key=lambda x: x[1])
    mapping = {op_val: idx for idx, (_, op_val) in enumerate(sorted_ops)}
    _a(f"                {dt} = {mapping!r}")
    _a(f"                {hi} = {dt}.get({v['op']}, -1)")

    #
    first = True
    for handler_idx, (op_name, op_val) in enumerate(sorted_ops):
        kw = 'if' if first else 'elif'
        first = False
        _a(f"                {kw} {hi} == {handler_idx}:")
        # emit the same handler body — reuse _gen_single_handler
        _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid)
    _a(f"                else: {pc} += 1")


def _gen_single_handler(lines, v, op_name, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, uid, indent='                    '):
    _a = lines.append
    I = indent  # shorthand

    def u8():
        return f"{code}[{pc}+1]"
    def u16():
        return f"({code}[{pc}+1] | ({code}[{pc}+2] << 8))"

    if op_name == 'PUSH_CONST':
        _a(f"{I}{stk}.append({consts}[{u8()}]); {pc} += 2")
    elif op_name == 'LOAD_LOCAL':
        _a(f"{I}{stk}.append({loc}[{u8()}]); {pc} += 2")
    elif op_name == 'STORE_LOCAL':
        _a(f"{I}{loc}[{u8()}] = {stk}.pop(); {pc} += 2")
    elif op_name == 'LOAD_GLOBAL':
        _a(f"{I}{stk}.append({gl}[{names}[{u8()}]]); {pc} += 2")
    elif op_name == 'STORE_GLOBAL':
        _a(f"{I}{gl}[{names}[{u8()}]] = {stk}.pop(); {pc} += 2")
    elif op_name == 'DUP':
        _a(f"{I}{stk}.append({stk}[-1]); {pc} += 1")
    elif op_name == 'POP':
        _a(f"{I}{stk}.pop(); {pc} += 1")
    elif op_name == 'ROT2':
        _a(f"{I}{stk}[-1], {stk}[-2] = {stk}[-2], {stk}[-1]; {pc} += 1")
    elif op_name in ('ADD','SUB','MUL','MOD','FLOORDIV','POW','BITXOR','BITAND','BITOR','LSHIFT','RSHIFT'):
        py_op = {'ADD':'+','SUB':'-','MUL':'*','MOD':'%','FLOORDIV':'//','POW':'**',
                  'BITXOR':'^','BITAND':'&','BITOR':'|','LSHIFT':'<<','RSHIFT':'>>'}[op_name]
        _a(f"{I}{v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} {py_op} {v['b']}); {pc} += 1")
    elif op_name == 'NEG':
        _a(f"{I}{stk}.append(-{stk}.pop()); {pc} += 1")
    elif op_name == 'INVERT':
        _a(f"{I}{stk}.append(~{stk}.pop()); {pc} += 1")
    elif op_name == 'BOOL_NOT':
        _a(f"{I}{stk}.append(not {stk}.pop()); {pc} += 1")
    elif op_name in ('CMP_EQ','CMP_NE','CMP_LT','CMP_GT','CMP_LE','CMP_GE','CMP_IS','CMP_ISNOT','CMP_IN'):
        py_op = {'CMP_EQ':'==','CMP_NE':'!=','CMP_LT':'<','CMP_GT':'>','CMP_LE':'<=','CMP_GE':'>=',
                  'CMP_IS':'is','CMP_ISNOT':'is not','CMP_IN':'in'}[op_name]
        _a(f"{I}{v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} {py_op} {v['b']}); {pc} += 1")
    elif op_name == 'JMP':
        _a(f"{I}{pc} = {u16()}")
    elif op_name == 'JT':
        _a(f"{I}{pc} = {u16()} if {stk}.pop() else {pc} + 3")
    elif op_name == 'JF':
        _a(f"{I}{pc} = {u16()} if not {stk}.pop() else {pc} + 3")
    elif op_name == 'CALL_FUNC':
        _a(f"{I}{v['tmp']} = {u8()}")
        _a(f"{I}if {v['tmp']}: {v['val']} = {stk}[-{v['tmp']}:]; del {stk}[-{v['tmp']}:]")
        _a(f"{I}else: {v['val']} = []")
        _a(f"{I}{stk}.append({stk}.pop()(*{v['val']})); {pc} += 2")
    elif op_name == 'CALL_METHOD':
        _a(f"{I}{v['tmp']} = {code}[{pc}+2]")
        _a(f"{I}{v['val']} = [{stk}.pop() for _ in range({v['tmp']})][::-1]")
        _a(f"{I}{stk}.append(getattr({stk}.pop(), {names}[{code}[{pc}+1]])(*{v['val']})); {pc} += 3")
    elif op_name == 'LOAD_ATTR':
        _a(f"{I}{stk}.append(getattr({stk}.pop(), {names}[{u8()}])); {pc} += 2")
    elif op_name == 'STORE_ATTR':
        _a(f"{I}{v['val']} = {stk}.pop(); setattr({stk}.pop(), {names}[{u8()}], {v['val']}); {pc} += 2")
    elif op_name == 'BUILD_LIST':
        _a(f"{I}{v['tmp']} = {u8()}")
        _a(f"{I}if {v['tmp']}: {v['val']} = {stk}[-{v['tmp']}:]; del {stk}[-{v['tmp']}:]")
        _a(f"{I}else: {v['val']} = []")
        _a(f"{I}{stk}.append({v['val']}); {pc} += 2")
    elif op_name == 'BUILD_TUPLE':
        _a(f"{I}{v['tmp']} = {u8()}")
        _a(f"{I}if {v['tmp']}: {v['val']} = tuple({stk}[-{v['tmp']}:]); del {stk}[-{v['tmp']}:]")
        _a(f"{I}else: {v['val']} = ()")
        _a(f"{I}{stk}.append({v['val']}); {pc} += 2")
    elif op_name == 'BUILD_DICT':
        _a(f"{I}{v['tmp']} = {u8()}; {v['val']} = {{}}")
        _a(f"{I}for _ in range({v['tmp']}): {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {v['val']}[{v['a']}] = {v['b']}")
        _a(f"{I}{stk}.append({v['val']}); {pc} += 2")
    elif op_name == 'SUBSCRIPT':
        _a(f"{I}{v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']}[{v['b']}]); {pc} += 1")
    elif op_name == 'STORE_SUBSCRIPT':
        _a(f"{I}{v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {v['val']} = {stk}.pop(); {v['a']}[{v['b']}] = {v['val']}; {pc} += 1")
    elif op_name == 'UNPACK':
        _a(f"{I}{v['val']} = list({stk}.pop())[:{u8()}]; {stk}.extend(reversed({v['val']})); {pc} += 2")
    elif op_name == 'BUILD_SLICE':
        _a(f"{I}{v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append(slice({v['a']}, {v['b']})); {pc} += 1")
    elif op_name == 'ITER_NEW':
        _a(f"{I}{stk}.append(iter({stk}.pop())); {pc} += 1")
    elif op_name == 'ITER_NEXT':
        _a(f"{I}{v['val']} = next({stk}[-1], None)")
        _a(f"{I}if {v['val']} is None: {stk}.pop(); {pc} = {u16()}")
        _a(f"{I}else: {stk}.append({v['val']}); {pc} += 3")
    elif op_name == 'RET':
        _a(f"{I}return {stk}.pop()")
    elif op_name == 'HALT':
        _a(f"{I}return {stk}[-1] if {stk} else None")
    elif op_name == 'XFER_PUSH_SHARED':
        _a(f"{I}{shared}[{u8()}].append({stk}.pop()); {pc} += 2")
    elif op_name == 'XFER_POP_SHARED':
        _a(f"{I}{stk}.append({shared}[{u8()}].pop()); {pc} += 2")
    elif op_name == 'XFER_STORE_GREG':
        _a(f"{I}{gregs}[{u8()}] = {stk}.pop(); {pc} += 2")
    elif op_name == 'XFER_LOAD_GREG':
        _a(f"{I}{stk}.append({gregs}[{u8()}]); {pc} += 2")
    elif op_name == 'VM_YIELD':
        _a(f"{I}{pc} += 1; break")
    elif op_name == 'REG_LOAD':
        _a(f"{I}{regs}[{code}[{pc}+1]] = {loc}[{code}[{pc}+2]]; {pc} += 3")
    elif op_name == 'REG_STORE':
        _a(f"{I}{loc}[{code}[{pc}+2]] = {regs}[{code}[{pc}+1]]; {pc} += 3")
    elif op_name == 'REG_PUSH':
        _a(f"{I}{stk}.append({regs}[{u8()}]); {pc} += 2")
    elif op_name == 'REG_POP':
        _a(f"{I}{regs}[{u8()}] = {stk}.pop(); {pc} += 2")
    elif op_name == 'REG_MOV':
        _a(f"{I}{regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+2]]; {pc} += 3")
    elif op_name == 'REG_ADD':
        _a(f"{I}{regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+1]] + {regs}[{code}[{pc}+2]]; {pc} += 3")
    elif op_name == 'REG_SUB':
        _a(f"{I}{regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+1]] - {regs}[{code}[{pc}+2]]; {pc} += 3")
    elif op_name in ('LOAD_ADD', 'LOAD_SUB'):
        py_op = '+' if op_name == 'LOAD_ADD' else '-'
        _a(f"{I}{stk}.append({loc}[{u8()}]); {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} {py_op} {v['b']}); {pc} += 2")
    elif op_name == 'PUSH_STORE':
        _a(f"{I}{loc}[{code}[{pc}+2]] = {consts}[{code}[{pc}+1]]; {pc} += 3")
    elif op_name == 'LOAD2':
        _a(f"{I}{stk}.append({loc}[{code}[{pc}+1]]); {stk}.append({loc}[{code}[{pc}+2]]); {pc} += 3")
    elif op_name == 'DUP_STORE':
        _a(f"{I}{stk}.append({stk}[-1]); {loc}[{u8()}] = {stk}.pop(); {pc} += 2")
    elif op_name == 'LOAD_CMP':
        _a(f"{I}{stk}.append({loc}[{u8()}]); {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} < {v['b']}); {pc} += 2")
    elif op_name == 'NOP':
        _a(f"{I}{pc} += 1")
    elif op_name == 'SETUP_EXCEPT':
        eh_var = regs.replace('_regs', '_eh')
        _a(f"{I}{eh_var}.append({code}[{pc}+1] | ({code}[{pc}+2] << 8)); {pc} += 3")
    elif op_name == 'POP_EXCEPT':
        eh_var = regs.replace('_regs', '_eh')
        _a(f"{I}{eh_var}.pop(); {pc} += 1")
    elif op_name == 'MORPH':
        _a(f"{I}{v['tmp']} = {code}[{pc}+1] | ({code}[{pc}+2] << 8); {code}[{v['tmp']}] ^= {code}[{pc}+3]; {pc} += 4")
    else:
        _a(f"{I}{pc} += 1")


def _emit_handlers(lines, v, code, stk, pc, regs, loc, consts, names, gl, shared, gregs, op_defs, uid):
    _a = lines.append

    def u8():
        return f"{code}[{pc}+1]"
    def u16():
        return f"({code}[{pc}+1] | ({code}[{pc}+2] << 8))"

    first = True
    for op_name, op_val in sorted(op_defs.items(), key=lambda x: x[1]):
        kw = 'if' if first else 'elif'
        first = False
        _a(f"                {kw} {v['op']} == {op_val}:")

        if op_name == 'PUSH_CONST':
            _a(f"                    {stk}.append({consts}[{u8()}]); {pc} += 2")
        elif op_name == 'LOAD_LOCAL':
            _a(f"                    {stk}.append({loc}[{u8()}]); {pc} += 2")
        elif op_name == 'STORE_LOCAL':
            _a(f"                    {loc}[{u8()}] = {stk}.pop(); {pc} += 2")
        elif op_name == 'LOAD_GLOBAL':
            _a(f"                    {stk}.append({gl}[{names}[{u8()}]]); {pc} += 2")
        elif op_name == 'STORE_GLOBAL':
            _a(f"                    {gl}[{names}[{u8()}]] = {stk}.pop(); {pc} += 2")
        elif op_name == 'DUP':
            _a(f"                    {stk}.append({stk}[-1]); {pc} += 1")
        elif op_name == 'POP':
            _a(f"                    {stk}.pop(); {pc} += 1")
        elif op_name == 'ROT2':
            _a(f"                    {stk}[-1], {stk}[-2] = {stk}[-2], {stk}[-1]; {pc} += 1")
        elif op_name in ('ADD', 'SUB', 'MUL', 'MOD', 'FLOORDIV', 'POW',
                          'BITXOR', 'BITAND', 'BITOR', 'LSHIFT', 'RSHIFT'):
            py_op = {'ADD':'+','SUB':'-','MUL':'*','MOD':'%','FLOORDIV':'//','POW':'**',
                      'BITXOR':'^','BITAND':'&','BITOR':'|','LSHIFT':'<<','RSHIFT':'>>'}[op_name]
            _a(f"                    {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} {py_op} {v['b']}); {pc} += 1")
        elif op_name == 'NEG':
            _a(f"                    {stk}.append(-{stk}.pop()); {pc} += 1")
        elif op_name == 'INVERT':
            _a(f"                    {stk}.append(~{stk}.pop()); {pc} += 1")
        elif op_name == 'BOOL_NOT':
            _a(f"                    {stk}.append(not {stk}.pop()); {pc} += 1")
        elif op_name in ('CMP_EQ','CMP_NE','CMP_LT','CMP_GT','CMP_LE','CMP_GE','CMP_IS','CMP_ISNOT','CMP_IN'):
            py_op = {'CMP_EQ':'==','CMP_NE':'!=','CMP_LT':'<','CMP_GT':'>',
                      'CMP_LE':'<=','CMP_GE':'>=','CMP_IS':'is','CMP_ISNOT':'is not','CMP_IN':'in'}[op_name]
            _a(f"                    {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} {py_op} {v['b']}); {pc} += 1")
        elif op_name == 'JMP':
            _a(f"                    {pc} = {u16()}")
        elif op_name == 'JT':
            _a(f"                    {pc} = {u16()} if {stk}.pop() else {pc} + 3")
        elif op_name == 'JF':
            _a(f"                    {pc} = {u16()} if not {stk}.pop() else {pc} + 3")
        elif op_name == 'CALL_FUNC':
            _a(f"                    {v['tmp']} = {u8()}")
            _a(f"                    if {v['tmp']}: {v['val']} = {stk}[-{v['tmp']}:]; del {stk}[-{v['tmp']}:]")
            _a(f"                    else: {v['val']} = []")
            _a(f"                    {stk}.append({stk}.pop()(*{v['val']})); {pc} += 2")
        elif op_name == 'CALL_METHOD':
            _a(f"                    {v['tmp']} = {code}[{pc}+2]")
            _a(f"                    {v['val']} = [{stk}.pop() for _ in range({v['tmp']})][::-1]")
            _a(f"                    {stk}.append(getattr({stk}.pop(), {names}[{code}[{pc}+1]])(*{v['val']})); {pc} += 3")
        elif op_name == 'LOAD_ATTR':
            _a(f"                    {stk}.append(getattr({stk}.pop(), {names}[{u8()}])); {pc} += 2")
        elif op_name == 'STORE_ATTR':
            _a(f"                    {v['val']} = {stk}.pop(); setattr({stk}.pop(), {names}[{u8()}], {v['val']}); {pc} += 2")
        elif op_name == 'BUILD_LIST':
            _a(f"                    {v['tmp']} = {u8()}")
            _a(f"                    if {v['tmp']}: {v['val']} = {stk}[-{v['tmp']}:]; del {stk}[-{v['tmp']}:]")
            _a(f"                    else: {v['val']} = []")
            _a(f"                    {stk}.append({v['val']}); {pc} += 2")
        elif op_name == 'BUILD_TUPLE':
            _a(f"                    {v['tmp']} = {u8()}")
            _a(f"                    if {v['tmp']}: {v['val']} = tuple({stk}[-{v['tmp']}:]); del {stk}[-{v['tmp']}:]")
            _a(f"                    else: {v['val']} = ()")
            _a(f"                    {stk}.append({v['val']}); {pc} += 2")
        elif op_name == 'BUILD_DICT':
            _a(f"                    {v['tmp']} = {u8()}")
            _a(f"                    {v['val']} = {{}}")
            _a(f"                    for _ in range({v['tmp']}): {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {v['val']}[{v['a']}] = {v['b']}")
            _a(f"                    {stk}.append({v['val']}); {pc} += 2")
        elif op_name == 'SUBSCRIPT':
            _a(f"                    {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']}[{v['b']}]); {pc} += 1")
        elif op_name == 'STORE_SUBSCRIPT':
            _a(f"                    {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {v['val']} = {stk}.pop(); {v['a']}[{v['b']}] = {v['val']}; {pc} += 1")
        elif op_name == 'UNPACK':
            _a(f"                    {v['val']} = list({stk}.pop())[:{u8()}]; {stk}.extend(reversed({v['val']})); {pc} += 2")
        elif op_name == 'BUILD_SLICE':
            _a(f"                    {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append(slice({v['a']}, {v['b']})); {pc} += 1")
        elif op_name == 'ITER_NEW':
            _a(f"                    {stk}.append(iter({stk}.pop())); {pc} += 1")
        elif op_name == 'ITER_NEXT':
            _a(f"                    {v['val']} = next({stk}[-1], None)")
            _a(f"                    if {v['val']} is None: {stk}.pop(); {pc} = {u16()}")
            _a(f"                    else: {stk}.append({v['val']}); {pc} += 3")
        elif op_name == 'RET':
            _a(f"                    return {stk}.pop()")
        elif op_name == 'HALT':
            _a(f"                    return {stk}[-1] if {stk} else None")
        #
        elif op_name == 'XFER_PUSH_SHARED':
            _a(f"                    {shared}[{u8()}].append({stk}.pop()); {pc} += 2")
        elif op_name == 'XFER_POP_SHARED':
            _a(f"                    {stk}.append({shared}[{u8()}].pop()); {pc} += 2")
        elif op_name == 'XFER_STORE_GREG':
            _a(f"                    {gregs}[{u8()}] = {stk}.pop(); {pc} += 2")
        elif op_name == 'XFER_LOAD_GREG':
            _a(f"                    {stk}.append({gregs}[{u8()}]); {pc} += 2")
        elif op_name == 'VM_YIELD':
            _a(f"                    {pc} += 1; break")
        #
        elif op_name == 'REG_LOAD':
            _a(f"                    {regs}[{code}[{pc}+1]] = {loc}[{code}[{pc}+2]]; {pc} += 3")
        elif op_name == 'REG_STORE':
            _a(f"                    {loc}[{code}[{pc}+2]] = {regs}[{code}[{pc}+1]]; {pc} += 3")
        elif op_name == 'REG_PUSH':
            _a(f"                    {stk}.append({regs}[{u8()}]); {pc} += 2")
        elif op_name == 'REG_POP':
            _a(f"                    {regs}[{u8()}] = {stk}.pop(); {pc} += 2")
        elif op_name == 'REG_MOV':
            _a(f"                    {regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+2]]; {pc} += 3")
        elif op_name == 'REG_ADD':
            _a(f"                    {regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+1]] + {regs}[{code}[{pc}+2]]; {pc} += 3")
        elif op_name == 'REG_SUB':
            _a(f"                    {regs}[{code}[{pc}+1]] = {regs}[{code}[{pc}+1]] - {regs}[{code}[{pc}+2]]; {pc} += 3")
        elif op_name == 'LOAD_ADD':
            _a(f"                    {stk}.append({loc}[{u8()}]); {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} + {v['b']}); {pc} += 2")
        elif op_name == 'LOAD_SUB':
            _a(f"                    {stk}.append({loc}[{u8()}]); {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} - {v['b']}); {pc} += 2")
        elif op_name == 'PUSH_STORE':
            _a(f"                    {loc}[{code}[{pc}+2]] = {consts}[{code}[{pc}+1]]; {pc} += 3")
        elif op_name == 'LOAD2':
            _a(f"                    {stk}.append({loc}[{code}[{pc}+1]]); {stk}.append({loc}[{code}[{pc}+2]]); {pc} += 3")
        elif op_name == 'DUP_STORE':
            _a(f"                    {stk}.append({stk}[-1]); {loc}[{u8()}] = {stk}.pop(); {pc} += 2")
        elif op_name == 'LOAD_CMP':
            _a(f"                    {stk}.append({loc}[{u8()}]); {v['b']} = {stk}.pop(); {v['a']} = {stk}.pop(); {stk}.append({v['a']} < {v['b']}); {pc} += 2")
        elif op_name == 'NOP':
            _a(f"                    {pc} += 1")
        elif op_name == 'SETUP_EXCEPT':
            eh_var = regs.replace('_regs', '_eh')
            _a(f"                    {eh_var}.append({code}[{pc}+1] | ({code}[{pc}+2] << 8)); {pc} += 3")
        elif op_name == 'POP_EXCEPT':
            eh_var = regs.replace('_regs', '_eh')
            _a(f"                    {eh_var}.pop(); {pc} += 1")
        elif op_name == 'MORPH':
            _a(f"                    {v['tmp']} = {code}[{pc}+1] | ({code}[{pc}+2] << 8); {code}[{v['tmp']}] ^= {code}[{pc}+3]; {pc} += 4")
        else:
            _a(f"                    {pc} += 1")
