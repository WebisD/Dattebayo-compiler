from Interpreters.Expression import Expression
# from Interpreters.Interpreter import Interpreter
from Interpreters.RThread import ThreadWithReturnValue
from Tokens.TokenEnum import TokenEnum as te

"""
GLC

ElseDeclaration : TAIJUTSU, LBRACK , Expression , RBRACK

Expression : ExpressionVariable | ConditionExpr | WhileDeclaration | PrintDeclaration
"""


class ElseDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        # self.expression = Interpreter(token_index, token_array)

    def run_glc(self):
        try:
            self.else_dec_exp()
            return [True, self.token_index, f'valid else declaration']
        except:
            return [False, self.token_index, f'invalid else declaration']

    def else_dec_exp(self):
        # t_expression = ThreadWithReturnValue(target=self.expression.parser)

        self.eat(te.TAIJUTSU)
        self.eat(te.LBRACK)

        # t_expression.start()
        # result_expression = t_expression.join()

        self.eat(te.RBRACK)

        # if result_expression[0]:
        return True

        # self.error()
