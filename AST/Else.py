from AST.AST import AST


class Else(AST):
    def __init__(self, token, body):
        self.token = token
        self.body = body
