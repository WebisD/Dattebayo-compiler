from .AST import AST


class WhileAST(AST):
    def __init__(self, condition, scope):
        self.condition = condition
        self.scope = scope
