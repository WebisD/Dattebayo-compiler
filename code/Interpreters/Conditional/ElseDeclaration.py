import copy

from Interpreters.Expression import Expression
from Interpreters.RThread import ThreadWithReturnValue
from Tokens.TokenEnum import TokenEnum as te

from AST.ElseAST import ElseAST

"""
GLC

ElseDeclaration : TAIJUTSU, LBRACK , Expression , RBRACK

Expression : ExpressionVariable | ConditionExpr | WhileDeclaration | PrintDeclaration
"""


class ElseDeclaration(Expression):
    """ Performs the creation of an object of type ElseDeclaration

        :param token_index: index of list tokens
        :param token_array: list tokens
        :param interpreter: a copy of interpreter with all GLCs 
    """
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        super().__init__(token_index, token_array)
        self.expression = copy.deepcopy(interpreter)

    def run_glc(self):
        """ Run the GLC of ElseDeclaration and will return the node based on BinOp and custom logs.

        """
        try:
            result = self.else_dec_exp()
            return [True, self.token_index, f'valid else declaration', result]
        except Exception as e:
            a = e
            return [False, self.token_index, f'invalid else declaration', None]

    def else_dec_exp(self):
        """ Check the GLC of ElseDeclaration and return the Else AST. In addition, will
        execute the interpreter to check block of codes inside the else

        """
        self.eat(te.TAIJUTSU)
        self.eat(te.LBRACK)

        result_list = []

        while self.current_token.type != te.RBRACK:
            self.expression.token_index = self.token_index
            self.expression.current_token = self.current_token
            t_expression = ThreadWithReturnValue(target=self.expression.run_parser)

            t_expression.start()

            result_expression = t_expression.join()

            Expression.append_result(result_expression[2])

            if result_expression[0]:
                self.token_index = result_expression[1]
                self.current_token = self.tokens[self.token_index]
                result_list.append(result_expression[3])
            else:
                self.error()

        self.eat(te.RBRACK)

        node = ElseAST(scope=result_list)

        return node
