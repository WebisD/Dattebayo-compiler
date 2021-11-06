from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

"""
Expressions for math operations

expr : factor (PLUS factor)*
factor : STRING
"""


class StrOperation(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):
        try:
            result = self.expr()
            return [True, self.token_index, "string"]
        except Exception as e:
            return [False, self.token_index, None]

    def factor(self):
        """factor : STRING"""
        token = self.current_token
        self.eat(te.STRING)
        return token.value

    def expr(self):
        """expr : factor (PLUS factor)*"""
        result = self.factor()

        while self.current_token.type == te.FUUMASHURIKEN:
            token = self.current_token
            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)
                result = result + self.factor()
        return result
