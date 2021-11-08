from Interpreters.Expression import Expression
from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Conditional.IfDeclaration import IfDeclaration
from Interpreters.Conditional.ElseDeclaration import ElseDeclaration

"""
GLC

VariableExpression : IfDeclaration | IfDeclaration , ElseDeclaration

IfDeclaration : NINJUTSU , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK

ElseDeclaration : TAIJUTSU, LBRACK , Expression , RBRACK
"""

class ConditionalExpression(Expression):
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        super().__init__(token_index, token_array)
        self.if_dec = IfDeclaration(token_index, token_array, interpreter)
        self.else_dec = ElseDeclaration(token_index, token_array, interpreter)

    def run_glc(self):
        try:
            result = self.cond_exp()
            return [True, self.token_index, result[2]]
        except:
            return [False, self.token_index, f'invalid conditional expression']

    def cond_exp(self) -> bool or None:
        t_if_dec = ThreadWithReturnValue(target=self.if_dec.run_glc)
        t_else_dec = ThreadWithReturnValue(target=self.else_dec.run_glc)

        t_if_dec.start()
        t_else_dec.start()

        result_if_dec = t_if_dec.join()
        result_else_dec = t_else_dec.join()

        Expression.append_result(result_if_dec[2])
        Expression.append_result(result_else_dec[2])

        if result_if_dec[0]:
            self.token_index = result_if_dec[1]
            return result_if_dec
        elif result_else_dec[0]:
            self.token_index = result_else_dec[1]
            return result_else_dec

        self.error()