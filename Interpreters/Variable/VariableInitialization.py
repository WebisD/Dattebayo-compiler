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


class VariableInitialization(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):
        try:
            self.var_ini()
            return [True, self.token_index, None]
        except:
            return [False, self.token_index, None]

    def var_ini(self):
        self.error()
