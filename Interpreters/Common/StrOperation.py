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
            return [True, self.token_index, "valid string/ string operation", self.output_lines]
        except Exception as e:
            return [False, self.token_index, "invalid string/ string operation"]

    def factor(self):
        """factor : STRING"""
        token = self.current_token

        if token.type == te.INTEGER:
            self.eat(te.INTEGER)
        elif token.type == te.FLOAT:
            self.eat(te.FLOAT)
        elif token.type == te.STRING:
            self.eat(te.STRING)
        else:
            self.error()
        self.output_lines+=str(token.value)
        return token.value

    def expr(self):
        """expr : factor (PLUS factor)*"""
        result = self.factor()

        while self.current_token.type == te.FUUMASHURIKEN:
            token = self.current_token
            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)
                self.output_lines+=" " + str(te.FUUMASHURIKEN.value) + " "
                result = result + self.factor()
        return result
