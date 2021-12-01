from .AST import AST


class ElseAST(AST):
    def __init__(self, scope):
        self.scope = scope
