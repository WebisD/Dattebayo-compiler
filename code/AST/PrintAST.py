from .AST import AST


class PrintAST(AST):
    def __init__(self, value):
        self.value = value
