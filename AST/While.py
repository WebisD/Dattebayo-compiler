from AST.AST import AST


class While(AST):
    def __init__(self, token, params, body):
        self.token = token
        self.params = params
        self.body = body
