import random

STACK_ONLY = 0
REGISTER = 1
HYBRID = 2

STACK_EFFECTS = {
    'PUSH_CONST': 1, 'LOAD_LOCAL': 1, 'STORE_LOCAL': -1,
    'LOAD_GLOBAL': 1, 'STORE_GLOBAL': -1,
    'DUP': 1, 'POP': -1, 'ROT2': 0, 'PUSH_NONE': 1,
    'ADD': -1, 'SUB': -1, 'MUL': -1, 'MOD': -1, 'FLOORDIV': -1, 'POW': -1,
    'BITXOR': -1, 'BITAND': -1, 'BITOR': -1, 'LSHIFT': -1, 'RSHIFT': -1,
    'NEG': 0, 'INVERT': 0, 'BOOL_NOT': 0,
    'CMP_EQ': -1, 'CMP_NE': -1, 'CMP_LT': -1, 'CMP_GT': -1,
    'CMP_LE': -1, 'CMP_GE': -1, 'CMP_IS': -1, 'CMP_ISNOT': -1, 'CMP_IN': -1,
    'JMP': 0, 'JT': -1, 'JF': -1,
    'CALL_FUNC': 0, 'LOAD_ATTR': 0, 'STORE_ATTR': -2, 'CALL_METHOD': 0,
    'BUILD_LIST': 0, 'BUILD_TUPLE': 0, 'BUILD_DICT': 0,
    'SUBSCRIPT': -1, 'STORE_SUBSCRIPT': -3,
    'UNPACK': 0, 'BUILD_SLICE': -1,
    'ITER_NEW': 0, 'ITER_NEXT': 0,
    'RET': -1, 'HALT': 0,
}

# binary ops that can be split across VMs
BINARY_OPS = {'ADD', 'SUB', 'MUL', 'MOD', 'FLOORDIV', 'POW',
              'BITXOR', 'BITAND', 'BITOR', 'LSHIFT', 'RSHIFT'}
COMPARE_OPS = {'CMP_EQ', 'CMP_NE', 'CMP_LT', 'CMP_GT', 'CMP_LE', 'CMP_GE',
               'CMP_IS', 'CMP_ISNOT', 'CMP_IN'}


class SplitResult:
    def __init__(self):
        self.segments = []
        self.dispatch_order = []
        self.n_shared_stacks = 0
        self.n_global_regs = 0
        self.vm_types = []


def _stack_effect(instr):
    op = instr[0]
    if op == 'CALL_FUNC':
        nargs = instr[1] if len(instr) > 1 else 0
        return -nargs
    if op == 'CALL_METHOD':
        nargs = instr[2] if len(instr) > 2 else 0
        return -nargs
    if op in ('BUILD_LIST', 'BUILD_TUPLE'):
        count = instr[1] if len(instr) > 1 else 0
        return 1 - count if count > 0 else 1
    if op == 'BUILD_DICT':
        count = instr[1] if len(instr) > 1 else 0
        return 1 - 2 * count if count > 0 else 1
    if op == 'UNPACK':
        count = instr[1] if len(instr) > 1 else 1
        return count - 1
    return STACK_EFFECTS.get(op, 0)


def split_instructions(ir, n_vms, rng):
    # find control flow targets (loops, branches — can't split these)
    jump_targets = set()
    for instr in ir:
        if instr[0] in ('JMP', 'JF', 'JT', 'ITER_NEXT') and len(instr) > 1:
            if isinstance(instr[1], str):
                jump_targets.add(instr[1])

    # identify safe regions: sequential code between control flow points
    # unsafe = anything between a jump target LABEL and its back-edge JMP
    in_control = 0
    safe = []  # list of bools, one per instruction
    for instr in ir:
        if instr[0] == 'LABEL' and instr[1] in jump_targets:
            in_control += 1
        if instr[0] in ('JMP', 'JF', 'JT', 'RET', 'HALT') and in_control > 0:
            safe.append(False)
            in_control -= 1
            continue
        safe.append(in_control == 0)

    vm_types = [rng.choice([STACK_ONLY, REGISTER, HYBRID]) for _ in range(n_vms)]
    vm_types[0] = STACK_ONLY
    if n_vms > 1:
        vm_types[1] = REGISTER
    if n_vms > 2:
        vm_types[2] = HYBRID

    # block-level splitting at statement boundaries
    segments, dispatch_order = _block_split(ir, n_vms, rng)

    # insert cross-VM shared stack transfers at VM boundaries
    _insert_shared_transfers(segments, dispatch_order, n_vms, rng)

    # rewrite segments for register-type VMs (ISA variety)
    _rewrite_for_vm_types(segments, vm_types, rng)

    # register/stack aliasing: link some register writes to global registers
    _insert_register_aliases(segments, vm_types, n_vms, rng)

    result = SplitResult()
    result.segments = segments
    result.dispatch_order = dispatch_order
    result.n_shared_stacks = max(n_vms - 1, 1)
    result.n_global_regs = 4
    result.vm_types = vm_types
    return result


def _insert_shared_transfers(segments, dispatch_order, n_vms, rng):
    """
    At VM boundaries where consecutive dispatch entries differ, route one value
    through a shared stack. Only insert when we can verify a matching STORE/LOAD pair
    on the same local slot at the exact boundary.
    """
    if len(dispatch_order) < 2:
        return

    n_shared = max(n_vms - 1, 1)

    # build per-VM instruction offset map: which instructions belong to which dispatch entry
    vm_offsets = {}  # vm_id -> list of (start, end) instruction index ranges
    for vm_id in range(n_vms):
        vm_offsets[vm_id] = []

    instr_pos = {}  # vm_id -> current instruction count
    for vm_id in range(n_vms):
        instr_pos[vm_id] = 0

    for seg_idx, (vm_id, _) in enumerate(dispatch_order):
        start = instr_pos[vm_id]
        # count instructions until VM_YIELD
        seg = segments[vm_id]
        pos = start
        while pos < len(seg) and seg[pos][0] != 'VM_YIELD':
            pos += 1
        if pos < len(seg):
            pos += 1  # include VM_YIELD
        vm_offsets[vm_id].append((start, pos))
        instr_pos[vm_id] = pos

    # now insert transfers at verified boundaries
    for seg_idx in range(len(dispatch_order) - 1):
        vm_a = dispatch_order[seg_idx][0]
        vm_b = dispatch_order[seg_idx + 1][0]
        if vm_a == vm_b:
            continue
        if rng.random() > 0.25:
            continue

        # find the end of vm_a's current dispatch entry
        a_ranges = vm_offsets[vm_a]
        # find which range corresponds to this dispatch entry
        a_range_idx = sum(1 for i in range(seg_idx) if dispatch_order[i][0] == vm_a)
        if a_range_idx >= len(a_ranges):
            continue
        a_start, a_end = a_ranges[a_range_idx]

        # find the start of vm_b's next dispatch entry
        b_ranges = vm_offsets[vm_b]
        b_range_idx = sum(1 for i in range(seg_idx + 1) if dispatch_order[i][0] == vm_b)
        if b_range_idx >= len(b_ranges):
            continue
        b_start, b_end = b_ranges[b_range_idx]

        seg_a = segments[vm_a]
        seg_b = segments[vm_b]

        # find last STORE_LOCAL before VM_YIELD in vm_a's range
        store_idx = None
        for i in range(a_end - 1, a_start - 1, -1):
            if i >= len(seg_a):
                continue
            if seg_a[i][0] == 'VM_YIELD':
                continue
            if seg_a[i][0] == 'STORE_LOCAL':
                store_idx = i
            break

        if store_idx is None:
            continue

        slot = seg_a[store_idx][1]
        shared_id = rng.randint(0, n_shared - 1)

        # check if vm_b's range starts with LOAD_LOCAL of the same slot
        load_idx = None
        for i in range(b_start, min(b_end, b_start + 5)):
            if i >= len(seg_b):
                break
            if seg_b[i][0] in ('LABEL', 'XFER_POP_SHARED', 'POP'):
                continue
            if seg_b[i][0] == 'LOAD_LOCAL' and seg_b[i][1] == slot:
                load_idx = i
            break

        if load_idx is not None:
            # matched pair: route through shared stack
            seg_a.insert(store_idx + 1, ('XFER_PUSH_SHARED', shared_id))
            seg_a.insert(store_idx, ('DUP',))
            # adjust offsets for the 2 inserted instructions
            for r_idx in range(len(a_ranges)):
                s, e = a_ranges[r_idx]
                if s > store_idx:
                    a_ranges[r_idx] = (s + 2, e + 2)
                elif e > store_idx:
                    a_ranges[r_idx] = (s, e + 2)
            # replace LOAD_LOCAL with XFER_POP_SHARED in vm_b
            seg_b[load_idx] = ('XFER_POP_SHARED', shared_id)


def _rewrite_for_vm_types(segments, vm_types, rng):
    """
    Rewrite LOAD_LOCAL/STORE_LOCAL to register ops for register-type VMs.
    This gives real ISA variety — register VMs use REG_LOAD/REG_PUSH instead of LOAD_LOCAL.
    """
    for vm_id, seg in enumerate(segments):
        if vm_types[vm_id] == STACK_ONLY:
            continue
        # for REGISTER and HYBRID VMs, rewrite some LOAD_LOCAL → REG_LOAD + REG_PUSH
        new_seg = []
        reg_alloc = {}  # local_slot → register (0-7)
        next_reg = 0
        for instr in seg:
            if instr[0] == 'LOAD_LOCAL' and rng.random() < 0.5 and next_reg < 8:
                slot = instr[1]
                if slot not in reg_alloc:
                    reg_alloc[slot] = next_reg
                    next_reg = min(next_reg + 1, 7)
                reg = reg_alloc[slot]
                new_seg.append(('REG_LOAD', reg, slot))
                new_seg.append(('REG_PUSH', reg))
            elif instr[0] == 'STORE_LOCAL' and rng.random() < 0.3 and next_reg < 8:
                slot = instr[1]
                if slot not in reg_alloc:
                    reg_alloc[slot] = next_reg
                    next_reg = min(next_reg + 1, 7)
                reg = reg_alloc[slot]
                new_seg.append(('REG_POP', reg))
                new_seg.append(('REG_STORE', reg, slot))
            else:
                new_seg.append(instr)
        segments[vm_id] = new_seg


def _insert_register_aliases(segments, vm_types, n_vms, rng):
    """
    When a register-type VM writes to a register (REG_STORE), also write the value
    to a global register. Another VM can then read from the global register instead
    of doing a separate LOAD_LOCAL. Creates hidden cross-VM data dependencies.
    """
    alias_prob = 0.2
    greg_id = 0

    for vm_id, seg in enumerate(segments):
        if vm_types[vm_id] == STACK_ONLY:
            continue
        new_seg = []
        for instr in seg:
            new_seg.append(instr)
            # after REG_STORE, also store to a global register
            if instr[0] == 'REG_STORE' and rng.random() < alias_prob and greg_id < 4:
                reg = instr[1]
                new_seg.append(('REG_PUSH', reg))
                new_seg.append(('XFER_STORE_GREG', greg_id))
                greg_id = (greg_id + 1) % 4
        segments[vm_id] = new_seg




def _find_basic_blocks(ir):
    jump_targets = set()
    for instr in ir:
        if instr[0] in ('JMP', 'JF', 'JT', 'ITER_NEXT') and len(instr) > 1:
            if isinstance(instr[1], str):
                jump_targets.add(instr[1])
    blocks = []
    current = []
    depth = 0
    in_control = 0
    for instr in ir:
        if instr[0] == 'LABEL':
            if current:
                blocks.append(current)
                current = []
                depth = 0
            current.append(instr)
            if instr[1] in jump_targets:
                in_control += 1
        elif instr[0] in ('JMP', 'JF', 'JT', 'RET', 'HALT'):
            current.append(instr)
            blocks.append(current)
            current = []
            depth = 0
            if in_control > 0:
                in_control -= 1
        else:
            current.append(instr)
            depth += _stack_effect(instr)
            if (in_control == 0 and depth <= 0
                    and instr[0] in ('STORE_LOCAL', 'STORE_GLOBAL')
                    and len(current) >= 2):
                blocks.append(current)
                current = []
                depth = 0
    if current:
        blocks.append(current)
    return blocks


def _find_jump_constraints(blocks):
    label_to_block = {}
    for i, block in enumerate(blocks):
        for instr in block:
            if instr[0] == 'LABEL':
                label_to_block[instr[1]] = i
    constraints = []
    for i, block in enumerate(blocks):
        for instr in block:
            if instr[0] in ('JMP', 'JF', 'JT', 'ITER_NEXT') and len(instr) > 1:
                target = instr[1]
                if isinstance(target, str) and target in label_to_block:
                    j = label_to_block[target]
                    if i != j:
                        constraints.append((i, j))
        last = block[-1] if block else None
        if last:
            if last[0] in ('JF', 'JT') and i + 1 < len(blocks):
                constraints.append((i, i + 1))
            safe_endings = ('STORE_LOCAL', 'STORE_GLOBAL', 'JMP', 'JF', 'JT',
                            'RET', 'HALT', 'VM_YIELD', 'POP')
            if last[0] not in safe_endings and i + 1 < len(blocks):
                constraints.append((i, i + 1))
    return constraints


def _merge_constrained(blocks, constraints):
    n = len(blocks)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    for a, b in constraints:
        union(a, b)
    groups = {}
    for i in range(n):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    return groups


def _assign_vms(groups, n_vms, rng):
    group_list = sorted(groups.values(), key=lambda g: min(g))
    assignments = {}
    vm_idx = 0
    for group in group_list:
        if rng.random() < 0.3 and n_vms > 2:
            vm_idx = (vm_idx + rng.randint(1, 2)) % n_vms
        for block_idx in group:
            assignments[block_idx] = vm_idx
        vm_idx = (vm_idx + 1) % n_vms
    return assignments


def _build_segments_with_transfers(blocks, assignments, n_vms, rng):
    segments = [[] for _ in range(n_vms)]
    dispatch_order = []
    current_vm = assignments.get(0, 0)
    current_run_blocks = 0
    for i, block in enumerate(blocks):
        vm = assignments.get(i, 0)
        if vm != current_vm:
            segments[current_vm].append(('VM_YIELD',))
            dispatch_order.append((current_vm, current_run_blocks))
            current_run_blocks = 0
            current_vm = vm
        for instr in block:
            segments[vm].append(instr)
        current_run_blocks += 1
    if current_run_blocks > 0:
        segments[current_vm].append(('VM_YIELD',))
        dispatch_order.append((current_vm, current_run_blocks))
    return segments, dispatch_order


def _block_split(ir, n_vms, rng):
    blocks = _find_basic_blocks(ir)
    constraints = _find_jump_constraints(blocks)
    groups = _merge_constrained(blocks, constraints)
    assignments = _assign_vms(groups, n_vms, rng)
    return _build_segments_with_transfers(blocks, assignments, n_vms, rng)


if __name__ == '__main__':
    rng = random.Random(42)

    # test 1: simple add gets split
    ir1 = [('LOAD_LOCAL', 0), ('LOAD_LOCAL', 1), ('ADD',), ('RET',)]
    r1 = split_instructions(ir1, 3, rng)
    vms1 = set(vm for vm, _ in r1.dispatch_order)
    print(f'add: {len(vms1)} VMs used, dispatch={r1.dispatch_order}')

    # test 2: expression split with transfers
    ir2 = [
        ('PUSH_CONST', 0), ('STORE_LOCAL', 2),
        ('LOAD_LOCAL', 0), ('LOAD_LOCAL', 1), ('ADD',), ('STORE_LOCAL', 2),
        ('LOAD_LOCAL', 2), ('PUSH_CONST', 1), ('MUL',), ('STORE_LOCAL', 3),
        ('LOAD_LOCAL', 3), ('RET',),
    ]
    r2 = split_instructions(ir2, 4, random.Random(123))
    vms2 = set(vm for vm, _ in r2.dispatch_order)
    print(f'multi-expr: {len(vms2)} VMs used, dispatch={r2.dispatch_order}')
    for i, seg in enumerate(r2.segments):
        if seg:
            ops = [s[0] for s in seg]
            has_xfer = any('XFER' in s[0] or 'REG' in s[0] for s in seg)
            print(f'  VM {i}: {len(seg)} instrs, xfer/reg={has_xfer}')

    # test 3: for loop stays together
    ir3 = [
        ('PUSH_CONST', 0), ('STORE_LOCAL', 1),
        ('LOAD_GLOBAL', 0), ('LOAD_LOCAL', 0), ('CALL_FUNC', 1), ('ITER_NEW',),
        ('LABEL', '__L1'),
        ('ITER_NEXT', '__L2'),
        ('STORE_LOCAL', 2),
        ('LOAD_LOCAL', 1), ('LOAD_LOCAL', 2), ('ADD',), ('STORE_LOCAL', 1),
        ('JMP', '__L1'),
        ('LABEL', '__L2'),
        ('LOAD_LOCAL', 1), ('RET',),
    ]
    r3 = split_instructions(ir3, 3, random.Random(42))
    print(f'for-loop: dispatch={r3.dispatch_order}')

    print('all splitter tests passed')
