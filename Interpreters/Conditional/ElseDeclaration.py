import copy

from Interpreters.Expression import Expression
from Interpreters.RThread import ThreadWithReturnValue
from Tokens.TokenEnum import TokenEnum as te

"""
GLC

ElseDeclaration : TAIJUTSU, LBRACK , Expression , RBRACK

Expression : ExpressionVariable | ConditionExpr | WhileDeclaration | PrintDeclaration
"""


class ElseDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        super().__init__(token_index, token_array)
        self.expression = copy.deepcopy(interpreter)

    def run_glc(self):
        try:
            self.else_dec_exp()
            return [True, self.token_index, f'valid else declaration']
        except:
            return [False, self.token_index, f'invalid else declaration']

    def else_dec_exp(self):
        self.eat(te.TAIJUTSU)
        self.output_lines+= te.TAIJUTSU.value
        self.eat(te.LBRACK)
        self.output_lines+= ":\n"
        self.append_to_file()
        self.expression.token_index = self.token_index
        self.expression.current_token = self.current_token
        t_expression = ThreadWithReturnValue(target=self.expression.parser)
        t_expression.start()
        result_expression = t_expression.join()

        Expression.append_result(result_expression[2])

        if result_expression[0]:
            self.token_index = result_expression[1]
            self.current_token = self.tokens[self.token_index]
        else:
            self.error()

        self.append_to_file()
        return True
