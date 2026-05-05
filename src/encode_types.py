import ast

def get_type_annotation(annotation):
    if isinstance(annotation, ast.Name):
        return annotation.id
    if isinstance(annotation, ast.Attribute):
        return annotation.attr
    if isinstance(annotation, ast.Subscript):
        if isinstance(annotation.value, ast.Name):
            return annotation.value.id
    return None
