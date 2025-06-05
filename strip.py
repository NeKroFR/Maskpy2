import ast
import astunparse

counter = 1
maskBank = {}

class Variable:
    def __init__(self, name, mask):
        self.name = name
        self.mask = mask

class Env:
    def __init__(self, variables):
        self.variables = variables

    def get(self, name):
        for var in self.variables:
            if var.name == name:
                return var
        return None

class File:
    def __init__(self, tree, file_name):
        self.tree = tree
        self.file_name = file_name
        self.imports = []
        self.import_from = []
        self.variables = []

    def getAll(self):
        return self.variables + self.imports + self.import_from

def mask_name():
    global counter
    name = f"X{counter:06d}"
    counter += 1
    return name

def mask_module(file):
    global maskBank
    for node in ast.walk(file.tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                module_name = name.name.split('.')[0]
                if module_name not in maskBank:
                    maskBank[module_name] = mask_name()
                file.imports.append(Variable(module_name, maskBank[module_name]))
                if name.asname:
                    if name.asname not in maskBank:
                        maskBank[name.asname] = mask_name()
                    file.imports.append(Variable(name.asname, maskBank[name.asname]))
        elif isinstance(node, ast.ImportFrom):
            module_name = node.module.split('.')[0] if node.module else ""
            if module_name and module_name not in maskBank:
                maskBank[module_name] = mask_name()
                file.imports.append(Variable(module_name, maskBank[module_name]))
            for name in node.names:
                item_name = name.name
                if item_name not in maskBank:
                    maskBank[item_name] = mask_name()
                alias = name.asname if name.asname else item_name
                if alias not in maskBank:
                    maskBank[alias] = mask_name()
                file.import_from.append(Variable(alias, maskBank[alias]))
        elif isinstance(node, ast.FunctionDef):
            if node.name not in maskBank:
                maskBank[node.name] = mask_name()
            file.variables.append(Variable(node.name, maskBank[node.name]))
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            if node.id not in maskBank:
                maskBank[node.id] = mask_name()
            file.variables.append(Variable(node.id, maskBank[node.id]))

def strip_imports(tree):
    """
    Transform all import statements to use aliases
    - import module -> import module as X000001
    - from module import item -> from module import item as X000002
    - from module import item1, item2 -> from module import item1 as X000003, item2 as X000004
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                module_name = name.name.split('.')[0]
                if module_name in maskBank:
                    name.asname = maskBank[module_name]
        elif isinstance(node, ast.ImportFrom):
            for name in node.names:
                item_name = name.name
                if item_name in maskBank:
                    name.asname = maskBank[item_name]

def strip_childs(node, env):
    for child in ast.iter_child_nodes(node):
        if isinstance(child, ast.Name):
            var = env.get(child.id)
            if var:
                child.id = var.mask
        elif isinstance(child, ast.FunctionDef):
            var = env.get(child.name)
            if var:
                child.name = var.mask
        elif isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
            var = env.get(child.func.id)
            if var:
                child.func.id = var.mask
        strip_childs(child, env)

def strip(code):
    """
    Obfuscate the input Python code string by:
    1. Removing comments (handled by ast.parse).
    2. Obfuscating imports (e.g., 'import os' -> 'import os as X...').
    3. Renaming variables and function names.
    Returns the obfuscated code as a string.
    """
    global counter, maskBank
    counter = 1
    maskBank = {}

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise ValueError(f"Invalid Python code: {e}")

    file = File(tree, "code.py")
    mask_module(file)
    strip_imports(tree)
    env = Env(file.getAll())
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            var = env.get(node.name)
            if var:
                node.name = var.mask
    for node in tree.body:
        strip_childs(node, env)

    stripped_code = astunparse.unparse(tree).strip()
    return stripped_code
