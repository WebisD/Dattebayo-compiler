from AST.AST import AST


class Print(AST):
    def __init__(self, token, params):
        self.token = token
        self.params = params
