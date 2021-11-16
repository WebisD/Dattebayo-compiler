from Tokens.TokenEnum import TokenEnum


class Token(object):
    def __init__(self, type: TokenEnum, value, regex=None, python_code=None):
        self.type: TokenEnum = type
        self.value = value
        self.regex = regex

    def __str__(self):
        return f"Token({self.type}, {self.value}, {self.regex})"

    def __repr__(self):
        return self.__str__()
