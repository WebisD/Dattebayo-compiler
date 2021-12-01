from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression

from Interpreters.Common.NumOperation import NumOperation
from Interpreters.Common.StrOperation import StrOperation
from Interpreters.Common.VarOperation import VarOperation

from AST.BoolAST import Bool
from AST.VariableAST import VariableAST
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
        self.var_operation = VarOperation(token_index, token_array)

    def run_glc(self):
        try:
            result = self.values_glc()
            return result
        except Exception as e:
            return [False, self.token_index, None, None]

    def values_glc(self):
        """Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation"""
        token = self.current_token
        type_value = None
        node = None

        if token.type == te.INTEGER or token.type == te.FLOAT:
            result = self.check_num_operation()
            if result is not None:
                type_value = result[0]
                node = result[1]
            else:
                self.error()
        elif token.type == te.STRING:
            result = self.check_str_operation()
            if result is not None:
                type_value = result[0]
                node = result[1]
            else:
                self.error()
        elif token.type == te.BOOLEAN:
            self.eat(te.BOOLEAN)
            type_value = "Boolean"
            node = Bool(token)
        elif token.type == te.IDENTIFIER:
            result = self.check_var_operation()
            if result is not None:
                type_value = result[0]
                node = result[1]
            else:
                self.error()
        else:
            self.error()

        return [True, self.token_index, type_value, node]

    def check_num_operation(self):
        self.num_operation = NumOperation(self.token_index, self.tokens)
        num_op = self.num_operation.run_glc()

        if num_op[0]:
            self.marker_index = num_op[1]
            self.update_interpreter_params()

        return num_op[2], num_op[3]

    def check_str_operation(self):
        self.str_operation = StrOperation(self.token_index, self.tokens)
        str_op = self.str_operation.run_glc()

        if str_op[0]:
            self.marker_index = str_op[1]
            self.update_interpreter_params()

        return str_op[2], str_op[3]

    def check_var_operation(self):
        self.var_operation = VarOperation(self.token_index, self.tokens)
        var_op = self.var_operation.run_glc()

        if var_op[0]:
            self.marker_index = var_op[1]
            self.update_interpreter_params()

        return var_op[2], var_op[3]