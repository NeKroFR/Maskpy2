import ast
import random


class CFFTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        helper = CFFHelper()
        param_names = [arg.arg for arg in node.args.args]
        if node.args.vararg:
            param_names.append(node.args.vararg.arg)
        if node.args.kwarg:
            param_names.append(node.args.kwarg.arg)

        # collect assigned vars for pre-init
        assigned_vars = set()
        for n in ast.walk(node):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                assigned_vars.add(n.id)

        exclude_vars = {helper.state_var, helper.sub_var, helper.return_var,
                        helper.handler_var, helper.dispatch_var,
                        helper.pack_var, helper.mask_var}
        local_vars_to_init = (
            {v for v in assigned_vars if not v.startswith('encoded_')}
            - set(param_names) - exclude_vars
        )
        init_assigns = [
            ast.Assign(
                targets=[ast.Name(id=v, ctx=ast.Store())],
                value=ast.Constant(value=0))
            for v in local_vars_to_init
        ]

        # process body into state machine
        start_state = helper.process_statements(node.body, helper.exit_state)

        handler_info = []
        dispatch_entries = []
        real_state_ids = [s for s, _, _ in helper.keys]

        for idx, (block_state, block_code, handles_transition) in enumerate(helper.keys):
            encoded = helper.encode_state(block_state)
            if not handles_transition:
                block_code.extend(helper.assign_state(helper.exit_state))
            handler_info.append((block_code, block_state))
            dispatch_entries.append((encoded, idx))

        # initial state
        initial_state = helper.new_state()
        real_state_ids.append(initial_state)
        initial_encoded = helper.encode_state(initial_state)
        initial_idx = len(handler_info)
        handler_info.append((helper.assign_state(start_state), initial_state))
        dispatch_entries.append((initial_encoded, initial_idx))

        # bogus states
        for _ in range(random.randint(2, 5)):
            bogus_raw = helper.new_state()
            bogus_encoded = helper.encode_state(bogus_raw)
            bogus_idx = len(handler_info)
            handler_info.append((helper.generate_bogus_code(real_state_ids), bogus_raw))
            dispatch_entries.append((bogus_encoded, bogus_idx))

        # shuffle handlers
        n = len(handler_info)
        perm = list(range(n))
        random.shuffle(perm)
        inv_perm = [0] * n
        for new_pos, old_idx in enumerate(perm):
            inv_perm[old_idx] = new_pos

        shuffled_info = [handler_info[perm[i]] for i in range(n)]
        shuffled_entries = [(enc, inv_perm[idx]) for enc, idx in dispatch_entries]

        # build dispatch table from interleaved list
        vm = helper.val_mask
        interleaved = []
        for enc_key, shuf_idx in shuffled_entries:
            interleaved.append(enc_key)
            interleaved.append(shuf_idx)  # raw; masked by dict comprehension

        # shuffle pairs
        pairs = [(interleaved[i], interleaved[i + 1]) for i in range(0, len(interleaved), 2)]
        random.shuffle(pairs)
        interleaved = []
        for a, b in pairs:
            interleaved.append(a)
            interleaved.append(b)

        p_assign = ast.Assign(
            targets=[_name(helper.pack_var, store=True)],
            value=ast.List(
                elts=[ast.Constant(value=v) for v in interleaved],
                ctx=ast.Load()))

        vm_assign = ast.Assign(
            targets=[_name(helper.mask_var, store=True)],
            value=ast.Constant(value=vm))

        # _d = {_p[i]: _p[i+1] ^ _vm for i in range(0, len(_p), 2)}
        _ci = '_ci'
        dt_build = ast.Assign(
            targets=[_name(helper.dispatch_var, store=True)],
            value=ast.DictComp(
                key=ast.Subscript(
                    value=_name(helper.pack_var),
                    slice=_name(_ci), ctx=ast.Load()),
                value=ast.BinOp(
                    left=ast.Subscript(
                        value=_name(helper.pack_var),
                        slice=ast.BinOp(
                            left=_name(_ci), op=ast.Add(),
                            right=ast.Constant(value=1)),
                        ctx=ast.Load()),
                    op=ast.BitXor(),
                    right=_name(helper.mask_var)),
                generators=[ast.comprehension(
                    target=_name(_ci, store=True),
                    iter=ast.Call(
                        func=_name('range'), args=[
                            ast.Constant(value=0),
                            ast.Call(func=_name('len'),
                                     args=[_name(helper.pack_var)], keywords=[]),
                            ast.Constant(value=2)],
                        keywords=[]),
                    ifs=[], is_async=0)]))

        # while loop
        encoded_exit = helper.encode_state(helper.exit_state)
        while_test = ast.Compare(
            left=_name(helper.state_var), ops=[ast.NotEq()],
            comparators=[ast.Constant(value=encoded_exit)])

        # _hi = _d.get(_s, default) ^ _vm
        not_found_idx = n  # guaranteed not a valid handler index
        default_masked = not_found_idx ^ vm
        hi_lookup = ast.Assign(
            targets=[_name(helper.handler_var, store=True)],
            value=ast.BinOp(
                left=ast.Call(
                    func=ast.Attribute(
                        value=_name(helper.dispatch_var),
                        attr='get', ctx=ast.Load()),
                    args=[_name(helper.state_var),
                          ast.Constant(value=default_masked)],
                    keywords=[]),
                op=ast.BitXor(),
                right=_name(helper.mask_var)))

        # polymorphic handler dispatch: randomly choose style per function
        cff_dispatch_style = random.choice(['elif', 'tree'])

        if cff_dispatch_style == 'tree':
            # binary search tree dispatch on handler index
            chain = _build_tree_dispatch(
                shuffled_info, helper, real_state_ids, n)
        else:
            # standard if/elif chain (shuffled order)
            elif_order = list(range(n))
            random.shuffle(elif_order)
            chain = []
            for i in elif_order:
                code, raw_state = shuffled_info[i]
                if not code:
                    continue
                if random.random() < 0.4:
                    code = helper.wrap_guard(code, raw_state, real_state_ids)
                cond = ast.Compare(
                    left=_name(helper.handler_var), ops=[ast.Eq()],
                    comparators=[ast.Constant(value=i)])
                if_stmt = ast.If(test=cond, body=code, orelse=chain)
                chain = [if_stmt]

        while_loop = ast.While(
            test=while_test,
            body=[hi_lookup] + chain,
            orelse=[])

        # sentinel for for-loops
        sentinel_stmts = []
        if helper.needs_sentinel:
            sentinel_stmts.append(ast.Assign(
                targets=[_name(helper.sentinel_var, store=True)],
                value=ast.Call(func=_name('object'), args=[], keywords=[])))

        # Assemble
        init_state = ast.Assign(
            targets=[_name(helper.state_var, store=True)],
            value=ast.Constant(value=initial_encoded))
        init_sub = ast.Assign(
            targets=[_name(helper.sub_var, store=True)],
            value=ast.Constant(value=helper.sub_values.get(
                initial_state, helper.sub_init)))
        init_return = ast.Assign(
            targets=[_name(helper.return_var, store=True)],
            value=ast.Constant(value=0))
        return_stmt = ast.Return(value=_name(helper.return_var))

        node.body = (sentinel_stmts + init_assigns +
                     [p_assign, vm_assign, dt_build,
                      init_state, init_sub, init_return,
                      while_loop, return_stmt])
        return node


def _build_tree_dispatch(shuffled_info, helper, real_state_ids, n):
    # collect valid handlers
    handlers = []
    for i in range(n):
        code, raw_state = shuffled_info[i]
        if not code:
            continue
        if random.random() < 0.4:
            code = helper.wrap_guard(code, raw_state, real_state_ids)
        handlers.append((i, code))

    if not handlers:
        return [ast.Pass()]

    def build_tree(items):
        if not items:
            return [ast.Pass()]
        if len(items) == 1:
            idx, code = items[0]
            return [ast.If(
                test=ast.Compare(
                    left=_name(helper.handler_var), ops=[ast.Eq()],
                    comparators=[ast.Constant(value=idx)]),
                body=code,
                orelse=[ast.Pass()])]
        mid = len(items) // 2
        mid_val = items[mid][0]
        left_items = items[:mid]
        right_items = items[mid:]
        return [ast.If(
            test=ast.Compare(
                left=_name(helper.handler_var), ops=[ast.Lt()],
                comparators=[ast.Constant(value=mid_val)]),
            body=build_tree(left_items),
            orelse=build_tree(right_items))]

    # sort by handler index for balanced tree
    handlers.sort(key=lambda x: x[0])
    return build_tree(handlers)


def _name(id, store=False):
    return ast.Name(id=id, ctx=ast.Store() if store else ast.Load())


class CFFHelper:
    def __init__(self):
        self.keys = []
        self._used_states = set()
        self._loop_stack = []
        self._iter_count = 0
        self.needs_sentinel = False
        self.sentinel_var = f'_sn{random.randint(10, 99)}'

        # 3-key state cipher
        self.k1 = random.randint(1, 0xFFFFFFFF)
        self.k2 = random.randrange(1, 0xFFFFFFFF, 2)  # odd → bijective mod 2^32
        self.k3 = random.randint(1, 0xFFFFFFFF)

        # Value mask for handler indices
        self.val_mask = random.randint(0x1000, 0xFFFF)

        # Exit state
        self.exit_state = -random.randint(1, 9999)
        self._used_states.add(self.exit_state)

        # Randomized variable names
        self.state_var = f'_s{random.randint(100, 999)}'
        self.sub_var = f'_u{random.randint(100, 999)}'
        self.return_var = f'_r{random.randint(100, 999)}'
        self.handler_var = f'_h{random.randint(100, 999)}'
        self.dispatch_var = f'_d{random.randint(100, 999)}'
        self.pack_var = f'_p{random.randint(100, 999)}'
        self.mask_var = f'_m{random.randint(100, 999)}'

        # Sub-state tracking: each state has an expected _u value
        self.sub_init = random.randint(0, 0xFFFF)
        self.sub_values = {}
        self.sub_values[self.exit_state] = random.randint(0, 0xFFFF)

    def encode_state(self, raw):
        x = raw ^ self.k1
        x = (x * self.k2) & 0xFFFFFFFF
        x = x ^ self.k3
        return x

    def new_state(self):
        while True:
            state = random.randint(1000, 99999)
            if state not in self._used_states:
                self._used_states.add(state)
                self.sub_values[state] = random.randint(0, 0xFFFF)
                return state

    def _opaque_true(self):
        sv = _name(self.state_var)
        patterns = [
            lambda v: ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=v, op=ast.Mult(),
                        right=ast.BinOp(left=v, op=ast.Add(), right=ast.Constant(value=1))),
                    op=ast.Mod(), right=ast.Constant(value=2)),
                ops=[ast.Eq()], comparators=[ast.Constant(value=0)]),
            lambda v: ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(
                        left=ast.BinOp(left=v, op=ast.Pow(), right=ast.Constant(value=2)),
                        op=ast.Add(), right=v),
                    op=ast.BitAnd(), right=ast.Constant(value=1)),
                ops=[ast.Eq()], comparators=[ast.Constant(value=0)]),
            lambda v: ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=v, op=ast.Pow(), right=ast.Constant(value=2)),
                    op=ast.Mod(), right=ast.Constant(value=4)),
                ops=[ast.NotEq()], comparators=[ast.Constant(value=3)]),
            lambda v: ast.Compare(
                left=ast.BinOp(left=v, op=ast.BitOr(),
                    right=ast.UnaryOp(op=ast.Invert(), operand=v)),
                ops=[ast.Eq()], comparators=[ast.Constant(value=-1)]),
            lambda v: ast.Compare(
                left=ast.BinOp(left=v, op=ast.BitAnd(), right=v),
                ops=[ast.Eq()], comparators=[v]),
            lambda v: ast.Compare(
                left=ast.BinOp(left=v, op=ast.BitXor(), right=v),
                ops=[ast.Eq()], comparators=[ast.Constant(value=0)]),
            lambda v: ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(
                        left=ast.BinOp(left=v, op=ast.Pow(), right=ast.Constant(value=3)),
                        op=ast.Sub(), right=v),
                    op=ast.Mod(), right=ast.Constant(value=6)),
                ops=[ast.Eq()], comparators=[ast.Constant(value=0)]),
        ]
        return random.choice(patterns)(sv)

    def assign_state(self, raw_target, opaque_prob=0.3):
        encoded = self.encode_state(raw_target)
        target_u = self.sub_values.get(raw_target, self.sub_init)
        stmts = []

        if random.random() < opaque_prob:
            bogus = random.randint(0, 0xFFFFFFFF)
            val = ast.IfExp(
                test=self._opaque_true(),
                body=ast.Constant(value=encoded),
                orelse=ast.Constant(value=bogus))
        else:
            val = ast.Constant(value=encoded)

        stmts.append(ast.Assign(
            targets=[_name(self.state_var, store=True)], value=val))

        # Always set sub-state to target's expected value
        stmts.append(ast.Assign(
            targets=[_name(self.sub_var, store=True)],
            value=ast.Constant(value=target_u)))

        return stmts

    def wrap_guard(self, code, raw_state, real_state_ids):
        expected_u = self.sub_values.get(raw_state, self.sub_init)
        guard_test = ast.Compare(
            left=_name(self.sub_var), ops=[ast.Eq()],
            comparators=[ast.Constant(value=expected_u)])

        bogus_target = random.choice(real_state_ids) if real_state_ids else self.exit_state
        bogus_code = [
            ast.Assign(
                targets=[_name(self.state_var, store=True)],
                value=ast.Constant(value=self.encode_state(bogus_target))),
            ast.Assign(
                targets=[_name(self.sub_var, store=True)],
                value=ast.Constant(value=random.randint(0, 0xFFFF)))
        ]
        return [ast.If(test=guard_test, body=code, orelse=bogus_code)]

    def generate_bogus_code(self, real_state_ids):
        code = []
        for _ in range(random.randint(1, 3)):
            var = _name(f'_t{random.randint(0, 999)}', store=True)
            val = ast.BinOp(
                left=_name(self.sub_var),
                op=random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.BitXor()]),
                right=ast.Constant(value=random.randint(0, 1000)))
            code.append(ast.Assign(targets=[var], value=val))
        target = random.choice(real_state_ids) if real_state_ids else self.exit_state
        code.extend(self.assign_state(target, opaque_prob=0.5))
        return code

    def process_statements(self, stmts, next_state):
        if not stmts:
            return next_state
        current = next_state
        for stmt in reversed(stmts):
            current = self.process_statement(stmt, current)
        return current

    def process_statement(self, stmt, next_state):
        if isinstance(stmt, ast.If):
            return self._process_if(stmt, next_state)
        elif isinstance(stmt, ast.Return):
            return self._process_return(stmt)
        elif isinstance(stmt, ast.While):
            return self._process_while(stmt, next_state)
        elif isinstance(stmt, ast.For):
            return self._process_for(stmt, next_state)
        elif isinstance(stmt, ast.Break):
            return self._process_break()
        elif isinstance(stmt, ast.Continue):
            return self._process_continue()
        else:
            return self._process_regular(stmt, next_state)

    def _process_if(self, stmt, next_state):
        then_start = self.process_statements(stmt.body, next_state)
        else_start = self.process_statements(stmt.orelse, next_state)
        cond_state = self.new_state()
        cond_code = [
            ast.If(test=stmt.test,
                   body=self.assign_state(then_start),
                   orelse=self.assign_state(else_start))
        ]
        self.keys.append((cond_state, cond_code, True))
        return cond_state

    def _process_return(self, stmt):
        ret_state = self.new_state()
        ret_code = [
            ast.Assign(
                targets=[_name(self.return_var, store=True)],
                value=stmt.value)
        ] + self.assign_state(self.exit_state)
        self.keys.append((ret_state, ret_code, True))
        return ret_state

    def _process_while(self, stmt, next_state):
        cond_state = self.new_state()
        if stmt.orelse:
            else_start = self.process_statements(stmt.orelse, next_state)
        else:
            else_start = next_state
        self._loop_stack.append((next_state, cond_state))
        body_start = self.process_statements(stmt.body, cond_state)
        self._loop_stack.pop()
        cond_code = [
            ast.If(test=stmt.test,
                   body=self.assign_state(body_start),
                   orelse=self.assign_state(else_start))
        ]
        self.keys.append((cond_state, cond_code, True))
        return cond_state

    def _process_for(self, stmt, next_state):
        self.needs_sentinel = True
        iter_var = f'_it{self._iter_count}'
        val_var = f'_vl{self._iter_count}'
        self._iter_count += 1
        init_state = self.new_state()
        check_state = self.new_state()
        if stmt.orelse:
            else_start = self.process_statements(stmt.orelse, next_state)
        else:
            else_start = next_state
        assign_target = ast.Assign(
            targets=[stmt.target],
            value=_name(val_var))
        body_stmts = [assign_target] + list(stmt.body)
        self._loop_stack.append((next_state, check_state))
        body_start = self.process_statements(body_stmts, check_state)
        self._loop_stack.pop()
        init_code = [
            ast.Assign(
                targets=[_name(iter_var, store=True)],
                value=ast.Call(func=_name('iter'),
                               args=[stmt.iter], keywords=[]))
        ] + self.assign_state(check_state)
        self.keys.append((init_state, init_code, True))
        next_call = ast.Call(
            func=_name('next'),
            args=[_name(iter_var), _name(self.sentinel_var)],
            keywords=[])
        check_code = [
            ast.Assign(targets=[_name(val_var, store=True)], value=next_call),
            ast.If(
                test=ast.Compare(
                    left=_name(val_var), ops=[ast.IsNot()],
                    comparators=[_name(self.sentinel_var)]),
                body=self.assign_state(body_start),
                orelse=self.assign_state(else_start))
        ]
        self.keys.append((check_state, check_code, True))
        return init_state

    def _process_break(self):
        if not self._loop_stack:
            return self.new_state()
        break_target = self._loop_stack[-1][0]
        block_state = self.new_state()
        self.keys.append((block_state, self.assign_state(break_target), True))
        return block_state

    def _process_continue(self):
        if not self._loop_stack:
            return self.new_state()
        continue_target = self._loop_stack[-1][1]
        block_state = self.new_state()
        self.keys.append((block_state, self.assign_state(continue_target), True))
        return block_state

    def _process_regular(self, stmt, next_state):
        block_state = self.new_state()
        block_code = [stmt] + self.assign_state(next_state)
        self.keys.append((block_state, block_code, True))
        return block_state
