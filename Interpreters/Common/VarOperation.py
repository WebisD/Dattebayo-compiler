from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

from AST.NumAST import Num
from AST.BinOp import BinOp
from AST.StringAST import Str
from AST.VariableAST import VariableAST


class VarOperation(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

    def run_glc(self):
        try:
            result = self.expr()
            return [True, self.token_index, "valid variable/variable operation", result]
        except Exception as e:
            return [False, self.token_index, "invalid variable/variable operation"]

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        node = None

        if token.type == te.INTEGER:
            self.eat(te.INTEGER)
            node = Num(token)
        elif token.type == te.FLOAT:
            self.eat(te.FLOAT)
            node = Num(token)
        elif token.type == te.STRING:
            self.eat(te.STRING)
            node = Str(Token)
        elif token.type == te.IDENTIFIER:
            self.eat(te.IDENTIFIER)
            node = VariableAST(name=token.value, value=None)
        else:
            self.error()

        return node

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