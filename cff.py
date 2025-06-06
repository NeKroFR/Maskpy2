import ast

class CFFTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        transformer = CFFHelper()
        param_names = [arg.arg for arg in node.args.args]
        assigned_vars = set()
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Name) and isinstance(stmt.ctx, ast.Store):
                assigned_vars.add(stmt.id)
        # Exclude parameters and state variables from initialization
        local_vars_to_init = assigned_vars - set(param_names) - {transformer.state_var, transformer.return_value_var}
        init_assigns = [ast.Assign(targets=[ast.Name(id=var, ctx=ast.Store())], value=ast.Constant(value=0)) for var in local_vars_to_init]
        start_state = transformer.process_statements(node.body, transformer.exit_state)
        state_var = transformer.state_var
        return_value_var = transformer.return_value_var
        while_loop = ast.While(
            test=ast.Compare(left=ast.Name(id=state_var, ctx=ast.Load()), ops=[ast.NotEq()], comparators=[ast.Num(transformer.exit_state)]),
            body=[],
            orelse=[]
        )

        # Collect state blocks
        state_blocks = []
        for block_state, block_code, handles_transition in transformer.keys:
            condition = ast.Compare(left=ast.Name(id=state_var, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Num(block_state)])
            if not handles_transition:
                block_code.append(ast.Assign(targets=[ast.Name(id=state_var, ctx=ast.Store())], value=ast.Num(transformer.exit_state)))
            state_blocks.append((condition, block_code))
        initial_state = transformer.new_state()
        initial_block = [ast.Assign(targets=[ast.Name(id=state_var, ctx=ast.Store())], value=ast.Num(start_state))]
        state_blocks.append((ast.Compare(left=ast.Name(id=state_var, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Num(initial_state)]), initial_block))

        # if-elif chain
        chain = []
        for condition, block in state_blocks:
            if_stmt = ast.If(test=condition, body=block, orelse=chain)
            chain = [if_stmt]
        while_loop.body = chain
        init_state = ast.Assign(targets=[ast.Name(id=state_var, ctx=ast.Store())], value=ast.Num(initial_state))
        init_return = ast.Assign(targets=[ast.Name(id=return_value_var, ctx=ast.Store())], value=ast.Constant(value=0))

        # Combine all parts into the new function body
        node.body = init_assigns + [init_state, init_return, while_loop, ast.Return(value=ast.Name(id=return_value_var, ctx=ast.Load()))]
        return node

class CFFHelper:
    def __init__(self):
        self.keys = []  # Stores (state, block_code, handles_transition)
        self.current_state = 0
        self.exit_state = -1
        self.state_var = 'state'
        self.return_value_var = 'return_value'

    def new_state(self):
        state = self.current_state
        self.current_state += 1
        return state

    def process_statements(self, stmts, next_state):
        if not stmts:
            return next_state
        current_state = next_state
        for stmt in reversed(stmts):
            current_state = self.process_statement(stmt, current_state)
        return current_state

    def process_statement(self, stmt, next_state):
        if isinstance(stmt, ast.If):
            then_start = self.process_statements(stmt.body, next_state)
            else_start = self.process_statements(stmt.orelse, next_state)
            condition_state = self.new_state()
            condition_code = [
                ast.If(
                    test=stmt.test,
                    body=[ast.Assign(targets=[ast.Name(id=self.state_var, ctx=ast.Store())], value=ast.Num(then_start))],
                    orelse=[ast.Assign(targets=[ast.Name(id=self.state_var, ctx=ast.Store())], value=ast.Num(else_start))]
                )
            ]
            self.keys.append((condition_state, condition_code, True))
            return condition_state
        elif isinstance(stmt, ast.Return):
            return_state = self.new_state()
            return_code = [
                ast.Assign(targets=[ast.Name(id=self.return_value_var, ctx=ast.Store())], value=stmt.value),
                ast.Assign(targets=[ast.Name(id=self.state_var, ctx=ast.Store())], value=ast.Num(self.exit_state))
            ]
            self.keys.append((return_state, return_code, True))
            return return_state
        else:
            block_state = self.new_state()
            block_code = [
                stmt,
                ast.Assign(targets=[ast.Name(id=self.state_var, ctx=ast.Store())], value=ast.Num(next_state))
            ]
            self.keys.append((block_state, block_code, True))
            return block_state
