from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

from AST.AST import AST
from AST.BinOp import BinOp
from AST.StringAST import Str

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
            return [True, self.token_index, "valid string/ string operation", result]
        except Exception as e:
            return [False, self.token_index, "invalid string/ string operation", None]

    def factor(self):
        """factor : STRING"""
        token = self.current_token

        self.eat(te.STRING)

        return Str(token)

    def expr(self):
        """expr : factor (PLUS factor)*"""
        node = self.factor()

        while self.current_token.type == te.FUUMASHURIKEN:
            token = self.current_token

            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)

            node = BinOp(left=node, op=token, right=self.factor())

        return node
