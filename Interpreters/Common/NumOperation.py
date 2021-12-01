from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

from AST.NumAST import Num
from AST.BinOp import BinOp

"""
Expressions for math operations

expr : term ((PLUS | MINUS) term)*
term : factor ((MUL | DIV) factor)*
factor : INTEGER
"""


class NumOperation(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):
        try:
            result = self.expr()
            return [True, self.token_index, "valid number/number operation", result]
        except Exception as e:
            return [False, self.token_index, "invalid number/number operation"]

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        if token.type == te.INTEGER:
            self.eat(te.INTEGER)
        elif token.type == te.FLOAT:
            self.eat(te.FLOAT)
        else:
            self.error()
        return Num(token)

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (te.SHURIKEN, te.KATANA):
            token = self.current_token
            if token.type == te.SHURIKEN:
                self.eat(te.SHURIKEN)
            elif token.type == te.KATANA:
                self.eat(te.KATANA)
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """expr : term ((PLUS | MINUS) term)*"""
        node = self.term()

        while self.current_token.type in (te.FUUMASHURIKEN, te.KUNAI):
            token = self.current_token
            if token.type == te.FUUMASHURIKEN:
                self.eat(te.FUUMASHURIKEN)

            elif token.type == te.KUNAI:
                self.eat(te.KUNAI)

            node = BinOp(left=node, op=token, right=self.term())

        return node
