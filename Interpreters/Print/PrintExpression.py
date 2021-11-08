from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression
from Interpreters.Variable.VariableDeclaration import VariableDeclaration
from Interpreters.Variable.VariableInitialization import VariableInitialization
from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Common.Values import Values

"""
                                    GLC
PrintDeclaration ⇐ SHARINGAN , LPAREN , Values , RPAREN , ENDPOINT ;
"""


class PrintExpression(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        self.values_interpreter = Values(token_index, token_array)

    def run_glc(self):
        try:
            result = self.print_glc()
            return [True, self.token_index, f"Print with {result[2]}"]
        except Exception as e:
            return [False, self.token_index, 'invalid print']

    def print_glc(self):
        """PrintDeclaration ⇐ SHARINGAN , LPAREN , Values , RPAREN , ENDPOINT ;"""
        self.eat(te.SHARINGAN)
        self.eat(te.LPAREN)
        type_value = self.check_value_params()
        self.eat(te.RPAREN)
        self.end_point()

        return type_value

    def check_value_params(self):
        self.values_interpreter = Values(self.token_index, self.tokens)
        type_value = self.values_interpreter.run_glc()

        if type_value[0]:
            self.marker_index = type_value[1]
            self.update_interpreter_params()

        return type_value
