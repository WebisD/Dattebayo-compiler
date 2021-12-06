from .AST import AST


class IfAST(AST):
    def __init__(self, condition, scope):
        self.condition = condition
        self.scope = scope
