from AST.AST import AST


class Type(AST):
    def __init__(self, token, type, value):
        self.token = token
        self.type = type
        self.value = value
