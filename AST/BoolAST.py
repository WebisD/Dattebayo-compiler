from .AST import AST


class Bool(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
