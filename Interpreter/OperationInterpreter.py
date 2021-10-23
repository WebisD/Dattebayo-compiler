from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token


class OperationInterpreter():
    def __init__(self, token_array=[]):
        self.tokens = iter(token_array)
        self.current_token: Token = next(self.tokens)

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            try:
                self.current_token = next(self.tokens)
            except Exception as e:
                print(f"Erro {self.current_token}")
        else:
            self.error()

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat(te.INTEGER)
        return token.value

    def term(self):
        result = self.factor()

        while self.current_token.type in (te.SHURIKEN, te.KATANA):
            token = self.current_token
            if token.type == te.SHURIKEN:
                self.eat(te.SHURIKEN)
                result = result * self.factor()
            elif token.type == te.KATANA:
                self.eat(te.KATANA)
                result = result / self.factor()

        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (te.FUUMASHURIKEN, te.KUNAI):
            token = self.current_token
            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)
                result = result + self.term()
            elif token.type == te.KUNAI:
                self.eat(te.KUNAI)
                result = result - self.term()
        print(result)
        return result