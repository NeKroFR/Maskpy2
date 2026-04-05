import random

# VM types
STACK_ONLY = 0   # type A: pure stack machine (current VM)
REGISTER = 1     # type B: register-based (8 regs, load/store)
HYBRID = 2       # type C: stack + registers

VM_TYPES = [STACK_ONLY, REGISTER, HYBRID]

# register opcodes (Type B and C)
REG_OPS = {
    'REG_LOAD': 0x80,    # u8 reg, u8 local_slot — load local into register
    'REG_STORE': 0x81,   # u8 reg, u8 local_slot — store register to local
    'REG_PUSH': 0x82,    # u8 reg — push register value onto stack
    'REG_POP': 0x83,     # u8 reg — pop stack into register
    'REG_MOV': 0x84,     # u8 dst_reg, u8 src_reg
    'REG_ADD': 0x85,     # u8 dst_reg, u8 src_reg — dst += src
    'REG_SUB': 0x86,     # u8 dst_reg, u8 src_reg — dst -= src
}

# cross-VM transfer opcodes (all types)
XFER_OPS = {
    'XFER_PUSH_SHARED': 0x90,  # u8 stack_id — push TOS onto shared stack
    'XFER_POP_SHARED': 0x91,   # u8 stack_id — pop from shared stack to TOS
    'XFER_STORE_GREG': 0x92,   # u8 greg_id — pop TOS to global register
    'XFER_LOAD_GREG': 0x93,    # u8 greg_id — push global register
    'VM_YIELD': 0x94,          # no operand — yield control to dispatcher
}

# self-modifying bytecode
# polymorphic ISA padding
POLY_OPS = {
    'NOP': 0xFE,  # no operation, 1 byte — used for random instruction padding
}

# instruction sizes for new opcodes
REG_OP_SIZES = {
    'REG_LOAD': 3, 'REG_STORE': 3, 'REG_PUSH': 2, 'REG_POP': 2,
    'REG_MOV': 3, 'REG_ADD': 3, 'REG_SUB': 3,
}
XFER_OP_SIZES = {
    'XFER_PUSH_SHARED': 2, 'XFER_POP_SHARED': 2,
    'XFER_STORE_GREG': 2, 'XFER_LOAD_GREG': 2,
    'VM_YIELD': 1,
}

# stack effect table for ALL opcodes (positive = push, negative = pop)
STACK_EFFECTS = {
    'PUSH_CONST': 1, 'LOAD_LOCAL': 1, 'STORE_LOCAL': -1,
    'LOAD_GLOBAL': 1, 'STORE_GLOBAL': -1,
    'DUP': 1, 'POP': -1, 'ROT2': 0,
    'ADD': -1, 'SUB': -1, 'MUL': -1, 'MOD': -1, 'FLOORDIV': -1, 'POW': -1,
    'BITXOR': -1, 'BITAND': -1, 'BITOR': -1, 'LSHIFT': -1, 'RSHIFT': -1,
    'NEG': 0, 'INVERT': 0, 'BOOL_NOT': 0,
    'CMP_EQ': -1, 'CMP_NE': -1, 'CMP_LT': -1, 'CMP_GT': -1,
    'CMP_LE': -1, 'CMP_GE': -1, 'CMP_IS': -1, 'CMP_ISNOT': -1, 'CMP_IN': -1,
    'JMP': 0, 'JT': -1, 'JF': -1,
    'CALL_FUNC': 0,
    'LOAD_ATTR': 0, 'STORE_ATTR': -2, 'CALL_METHOD': 0,
    'BUILD_LIST': 0, 'BUILD_TUPLE': 0, 'BUILD_DICT': 0,
    'SUBSCRIPT': -1, 'STORE_SUBSCRIPT': -3,
    'UNPACK': 0, 'BUILD_SLICE': -1,
    'ITER_NEW': 0, 'ITER_NEXT': 0,
    'RET': -1, 'HALT': 0,
    # register ops
    'REG_LOAD': 0, 'REG_STORE': 0, 'REG_PUSH': 1, 'REG_POP': -1,
    'REG_MOV': 0, 'REG_ADD': 0, 'REG_SUB': 0,
    # transfer ops
    'XFER_PUSH_SHARED': -1, 'XFER_POP_SHARED': 1,
    'XFER_STORE_GREG': -1, 'XFER_LOAD_GREG': 1,
    'VM_YIELD': 0,
}

# compound opcode candidates: (name, [base_op1, base_op2], operand_spec)
COMPOUND_CANDIDATES = [
    ('LOAD_ADD', ['LOAD_LOCAL', 'ADD'], 'u8'),
    ('PUSH_STORE', ['PUSH_CONST', 'STORE_LOCAL'], 'u8u8'),
    ('LOAD2', ['LOAD_LOCAL', 'LOAD_LOCAL'], 'u8u8'),
    ('DUP_STORE', ['DUP', 'STORE_LOCAL'], 'u8'),
    ('LOAD_SUB', ['LOAD_LOCAL', 'SUB'], 'u8'),
    ('LOAD_CMP', ['LOAD_LOCAL', 'CMP_LT'], 'u8'),
]

def generate_compound_set(rng, count=2):
    chosen = rng.sample(COMPOUND_CANDIDATES, min(count, len(COMPOUND_CANDIDATES)))
    result = {}
    for i, (name, base_ops, operand_spec) in enumerate(chosen):
        result[name] = {
            'byte': 0xA0 + i,
            'base_ops': base_ops,
            'operand_spec': operand_spec,
        }
    return result

def generate_vm_config(vm_id, vm_type, master_seed, rng):
    from vm_interp import generate_opcode_table
    perm = generate_opcode_table(master_seed ^ (vm_id * 0x9E3779B9))
    compounds = generate_compound_set(rng) if rng.random() < 0.7 else {}
    return {
        'vm_id': vm_id,
        'vm_type': vm_type,
        'opcode_table': perm,
        'compounds': compounds,
    }

if __name__ == '__main__':
    rng = random.Random(42)

    # compound set: 2 entries with unique bytes
    cs = generate_compound_set(rng, count=2)
    assert len(cs) == 2
    bytes_used = [v['byte'] for v in cs.values()]
    assert len(set(bytes_used)) == 2

    # vm config has all required keys
    cfg = generate_vm_config(0, STACK_ONLY, 12345, random.Random(99))
    for k in ('vm_id', 'vm_type', 'opcode_table', 'compounds'):
        assert k in cfg, f'missing key: {k}'

    # stack effects covers all base opcodes
    from vm_compiler import OP
    for op_name in OP:
        assert op_name in STACK_EFFECTS, f'missing stack effect for {op_name}'

    print('all isa tests passed')
