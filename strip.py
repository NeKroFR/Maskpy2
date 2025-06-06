import ast
import astunparse

counter = 1

class RenameTransformer(ast.NodeTransformer):
    def __init__(self, mask_bank, function_local_vars):
        self.mask_bank = mask_bank
        self.function_local_vars = function_local_vars
        self.current_function = None

    def visit_FunctionDef(self, node):
        original_name = node.name
        node.name = self.mask_bank[("global", original_name)]
        for arg in node.args.args:
            arg.arg = self.mask_bank[(original_name, arg.arg)]
        self.current_function = original_name
        self.generic_visit(node)
        self.current_function = None
        return node

    def visit_Name(self, node):
        if self.current_function:
            local_key = (self.current_function, node.id)
            global_key = ("global", node.id)
            if local_key in self.mask_bank:
                node.id = self.mask_bank[local_key]
            elif global_key in self.mask_bank:
                node.id = self.mask_bank[global_key]
        else:
            global_key = ("global", node.id)
            if global_key in self.mask_bank:
                node.id = self.mask_bank[global_key]
        return node

    def visit_Call(self, node):
        self.generic_visit(node)
        return node

def collect_global_variables(tree):
    global_vars = set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            global_vars.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    global_vars.add(target.id)
        elif isinstance(node, ast.Import):
            for name in node.names:
                var_name = name.asname or name.name.split('.')[0]
                global_vars.add(var_name)
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                var_name = name.asname or name.name
                global_vars.add(var_name)
    return global_vars

def collect_local_variables(func_node):
    local_vars = set(arg.arg for arg in func_node.args.args)
    for node in ast.walk(func_node):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            local_vars.add(node.id)
    return local_vars

def strip_imports(tree, mask_bank):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                var_name = name.asname or name.name.split('.')[0]
                if ("global", var_name) in mask_bank:
                    name.asname = mask_bank[("global", var_name)]
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                var_name = name.asname or name.name
                if ("global", var_name) in mask_bank:
                    name.asname = mask_bank[("global", var_name)]

def strip(code):
    global counter
    counter = 1

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise ValueError(f"Invalid Python code: {e}")

    global_vars = collect_global_variables(tree)
    function_local_vars = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            function_local_vars[node.name] = collect_local_variables(node)

    mask_bank = {}
    for var in global_vars:
        mask_bank[("global", var)] = f"X{counter:06d}"
        counter += 1
    for func_name, local_vars in function_local_vars.items():
        for var in local_vars:
            mask_bank[(func_name, var)] = f"X{counter:06d}"
            counter += 1

    strip_imports(tree, mask_bank)

    transformer = RenameTransformer(mask_bank, function_local_vars)
    tree = transformer.visit(tree)
    ast.fix_missing_locations(tree)
    return astunparse.unparse(tree).strip()
