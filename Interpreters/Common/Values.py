from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

from Interpreters.OperationInterpreter import OperationInterpreter
from Interpreters.Common.Number import Number

"""
        Class for values accepted in variables and ifs condition

                                    GLC
Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation
Num : INT | FLOAT
NumOperation : (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ;
StrOperation : STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;
Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;
"""


class Values(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)

        self.num_operation = OperationInterpreter(token_index, token_array)

    def run_glc(self):
        try:
            result = self.values_glc()
            return result
        except Exception as e:
            return [False, self.token_index, None]

    def values_glc(self):
        token = self.current_token
        type_value = None

        if token.type == te.INTEGER:
            result = self.check_num_operation()
            if result is not None:
                type_value = result
            else:
                self.error()
        elif token.type == te.FLOAT:
            self.eat(te.FLOAT)
            type_value = "Number"
        elif token.type == te.STRING:
            self.eat(te.STRING)
            type_value = "String"
        elif token.type == te.BOOLEAN:
            self.eat(te.BOOLEAN)
            type_value = "Boolean"
        else:
            self.error()

        return [True, self.token_index, type_value]

    def check_num_operation(self):
        self.num_operation = OperationInterpreter(self.token_index, self.tokens)
        num_op = self.num_operation.run_glc()
        if num_op[0]:
            self.marker_index = num_op[1]
            self.update_interpreter_params()
        return num_op[2]

