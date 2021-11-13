from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression

from Interpreters.Common.NumOperation import NumOperation
from Interpreters.Common.StrOperation import StrOperation
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

        self.num_operation = NumOperation(token_index, token_array)
        self.str_operation = StrOperation(token_index, token_array)

    def run_glc(self):
        try:
            result = self.values_glc()
            return result
        except Exception as e:
            return [False, self.token_index, None]

    def values_glc(self):
        """Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation"""
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
            self.output_lines+=str(token.value)
            type_value = "Number"
        elif token.type == te.STRING:
            result = self.check_str_operation()
            if result is not None:
                type_value = result
            else:
                self.error()
        elif token.type == te.BOOLEAN:
            self.eat(te.BOOLEAN)
            self.output_lines+=str(token.value)
            type_value = "Boolean"
        else:
            self.error()

        return [True, self.token_index, type_value]

    def check_num_operation(self):
        self.num_operation = NumOperation(self.token_index, self.tokens)
        num_op = self.num_operation.run_glc()
        if num_op[0]:
            self.output_lines+=self.num_operation.output_lines
            self.marker_index = num_op[1]
            self.update_interpreter_params()
        return num_op[2]

    def check_str_operation(self):
        self.str_operation = StrOperation(self.token_index, self.tokens)
        str_op = self.str_operation.run_glc()
        if str_op[0]:
            self.output_lines+=self.str_operation.output_lines
            self.marker_index = str_op[1]
            self.update_interpreter_params()
        return str_op[2]
