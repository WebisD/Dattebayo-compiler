from .AST import AST


class VariableAST(AST):
    def __init__(self, name, value):
        self.name = name
        self.value = value
