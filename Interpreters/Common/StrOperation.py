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
        """ Performs the creation of an object of type StrOperation

        :param token_index: index of list tokens
        :param token_array: list tokens
        """
        super().__init__(token_index, token_array)

    def run_glc(self):
        """ Run the GLC of StrOperation and will return the node based on BinOp and custom logs.

        """
        try:
            result = self.expr()
            return [True, self.token_index, "valid string/ string operation", result]
        except Exception as e:
            return [False, self.token_index, "invalid string/ string operation", None]

    def factor(self):
        """ Gets the factor of operation 

        """
        token = self.current_token

        self.eat(te.STRING)

        return Str(token)

    def expr(self):
        """ Return the node of operation based on term and operation

        """
        node = self.factor()

        while self.current_token.type == te.FUUMASHURIKEN:
            token = self.current_token

            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)

            node = BinOp(left=node, op=token, right=self.factor())

        return node
