from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression
# from Interpreters.OperationInterpreter import OperationInterpreter
from Interpreters.Common.Values import Values

from AST.BinOp import BinOp

"""

ConditionParam ⇐ (Values , Comparators , Value) ;
"""


class ConditionParam(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        self.values_interpreter = Values(token_index, token_array)

    def run_glc(self):
        try:
            node = BinOp(left=self.check_type_value()[3], op=self.comparator(), right=self.check_type_value()[3])

            return [True, self.token_index, f'valid single condition', node]
        except:
            return [False, self.token_index, None, None]

    def check_type_value(self):
        self.values_interpreter = Values(self.token_index, self.tokens)
        type_value = self.values_interpreter.run_glc()

        Expression.append_result(type_value[2])

        if type_value[0]:
            self.marker_index = type_value[1]
            self.update_interpreter_params()
            return type_value
        
        self.error()

    def comparator(self):
        token = self.current_token

        if token.type == te.GENNIN:
            self.eat(te.GENNIN)
        elif token.type == te.JUNNIN:
            self.eat(te.JUNNIN)
        elif token.type == te.KIRIGAKURE:
            self.eat(te.KIRIGAKURE)
        else:
            self.error()

        return token
