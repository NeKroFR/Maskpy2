import random

def fuse_opcodes(ir_instructions, compound_defs, rng):
    if not compound_defs:
        return ir_instructions

    # build lookup: (op1, op2) -> compound_name
    pair_lookup = {}
    for name, info in compound_defs.items():
        ops = info['base_ops']
        pair_lookup[(ops[0], ops[1])] = (name, info)

    # don't fuse across labels, jumps, or control flow boundaries
    unsafe = {'LABEL', 'JMP', 'JF', 'JT', 'RET', 'HALT', 'ITER_NEXT', 'VM_YIELD',
              'XFER_PUSH_SHARED', 'XFER_POP_SHARED', 'XFER_STORE_GREG', 'XFER_LOAD_GREG',
              'CALL_FUNC', 'CALL_METHOD', 'UNPACK', 'BUILD_LIST', 'BUILD_TUPLE',
              'BUILD_DICT', 'STORE_SUBSCRIPT'}

    result = []
    i = 0
    while i < len(ir_instructions):
        if i + 1 < len(ir_instructions):
            instr1 = ir_instructions[i]
            instr2 = ir_instructions[i + 1]
            pair_key = (instr1[0], instr2[0])

            # only fuse when neither instruction is near control flow
            if (pair_key in pair_lookup
                    and instr1[0] not in unsafe and instr2[0] not in unsafe
                    and rng.random() < 0.5):
                # also check the instruction AFTER the pair isn't a label
                if i + 2 < len(ir_instructions) and ir_instructions[i + 2][0] == 'LABEL':
                    result.append(ir_instructions[i])
                    i += 1
                    continue
                name, info = pair_lookup[pair_key]
                if info['operand_spec'] == 'u8':
                    operand = instr1[1] if len(instr1) > 1 else 0
                    result.append((name, operand))
                elif info['operand_spec'] == 'u8u8':
                    op1 = instr1[1] if len(instr1) > 1 else 0
                    op2 = instr2[1] if len(instr2) > 1 else 0
                    result.append((name, op1, op2))
                else:
                    result.append((name,))
                i += 2
                continue

        result.append(ir_instructions[i])
        i += 1

    return result

if __name__ == '__main__':
    rng = random.Random(42)

    # test: fuse LOAD_LOCAL + ADD
    compounds = {
        'LOAD_ADD': {'byte': 0xA0, 'base_ops': ['LOAD_LOCAL', 'ADD'], 'operand_spec': 'u8'},
    }
    ir = [('PUSH_CONST', 5), ('LOAD_LOCAL', 2), ('ADD',), ('STORE_LOCAL', 0)]
    fused = fuse_opcodes(ir, compounds, rng)
    print(f'original: {ir}')
    print(f'fused:    {fused}')
    assert len(fused) <= len(ir)

    # test: empty compounds = no changes
    assert fuse_opcodes(ir, {}, rng) == ir

    # test: PUSH_STORE (u8u8)
    compounds2 = {
        'PUSH_STORE': {'byte': 0xA1, 'base_ops': ['PUSH_CONST', 'STORE_LOCAL'], 'operand_spec': 'u8u8'},
    }
    ir2 = [('PUSH_CONST', 0), ('STORE_LOCAL', 3)]
    any_fused = False
    for _ in range(20):
        f = fuse_opcodes(ir2, compounds2, random.Random(_))
        if len(f) == 1 and f[0][0] == 'PUSH_STORE':
            any_fused = True
            assert f[0] == ('PUSH_STORE', 0, 3)
            break
    assert any_fused

    print('all compound tests passed')
