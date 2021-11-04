from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

"""
Class for variables declaration without initialization

                        GLC
VariableDeclaration : VariableType IDENTIFIER ENDPOINT
VariableType : RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE
"""


class VariableDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):
        try:
            self.var_dec_glc()
            return [True, self.token_index, "Variable declaration"]
        except Exception as e:
            return [False, self.token_index, None]

    def var_dec_glc(self):
        self.variable_type()
        self.identifier()
        self.end_point()

    def variable_type(self):
        """VariableType : RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE"""

        token = self.current_token

        if token.type == te.RASENGAN:
            self.eat(te.RASENGAN)
        elif token.type == te.RAIKIRI:
            self.eat(te.RAIKIRI)
        elif token.type == te.ZETSU:
            self.eat(te.ZETSU)
        elif token.type == te.KUCHIYOSE:
            self.eat(te.KUCHIYOSE)
        else:
            self.error()

    def identifier(self):
        token = self.current_token

        self.eat(te.IDENTIFIER)
