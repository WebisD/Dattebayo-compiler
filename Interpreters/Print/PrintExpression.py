from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression
from Interpreters.Variable.VariableDeclaration import VariableDeclaration
from Interpreters.Variable.VariableInitialization import VariableInitialization
from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Common.Values import Values

from AST.PrintAST import PrintAST

"""
                                    GLC
PrintDeclaration ⇐ SHARINGAN , LPAREN , Values , RPAREN , ENDPOINT ;
"""


class PrintExpression(Expression):
    def __init__(self, token_index: int, token_array=None):
        """ Performs the creation of an object of type class PrintExpression,
        in addition will create the class that will interpret Values GLC

        :param token_index: index of list tokens
        :param token_array: list tokens
        """
        super().__init__(token_index, token_array)
        self.values_interpreter = Values(token_index, token_array)

    def run_glc(self):
        """ Run the PrintExpression of Values, checking every possible operation and will return the node and custom logs.

        """   
        try:
            result = self.print_glc()
            return [True, self.token_index, f"Print with {result[2]}", result[3]]
        except Exception as e:
            return [False, self.token_index, 'invalid print']

    def print_glc(self):
        """ Check the GLC of PrintExpression and return the Print AST

        """
        self.eat(te.SHARINGAN)
        self.eat(te.LPAREN)
        type_value = self.check_value_params()
        self.eat(te.RPAREN)
        self.end_point()

        node = PrintAST(value=type_value[3])
        type_value[3] = node

        return type_value

    def check_value_params(self):
        """ Will check the value params based on Values GLC

        """ 
        self.values_interpreter = Values(self.token_index, self.tokens)
        type_value = self.values_interpreter.run_glc()

        if type_value[0]:
            self.marker_index = type_value[1]
            self.update_interpreter_params()

        return type_value
