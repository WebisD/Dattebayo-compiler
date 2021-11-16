from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

"""
Num : INT | FLOAT
"""


class Number(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):

        try:
            token = self.current_token

            if token.type == te.INTEGER:
                self.eat(te.INTEGER)
            elif token.type == te.FLOAT:
                self.eat(te.FLOAT)
            else:
                self.error()
            return [True, self.token_index, "Number"]
        except Exception as e:
            return [False, self.token_index, None]
