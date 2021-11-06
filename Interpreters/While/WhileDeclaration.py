from Interpreters.Common.Values import Values
from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Variable.VariableExpression import VariableExpression
from Interpreters.While.MultipleConditionParam import MultipleConditionParam
from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression

"""
Class for variables declaration of while loop

                        GLC

WhileDeclaration ⇐ TSUKUYOMI , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

MultipleConditionParam ⇐ {[ConditionParam , Operator]} , ConditionParam ;

ConditionParam ⇐ (Values , Comparators , Value) ;
"""


class WhileDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        self.var_multiple = MultipleConditionParam(token_index, token_array)
        self.var_expr = VariableExpression(token_index, token_array)

    def run_glc(self):
        try:
            self.eat(te.TSUKUYOMI)
            self.eat(te.LPAREN)
            #result = self.var_mult_exp()
            self.eat(te.RPAREN)
            self.eat(te.LBRACK)
            result = self.var_exp()
            self.eat(te.RBRACK)

            self.end_point()
            return [True, self.token_index, f'valid while expression']
        except:
            return [False, self.token_index, None]

    def var_mult_exp(self):
        t_var_mult_exp = ThreadWithReturnValue(target=self.var_mult_exp.run_glc)

        t_var_mult_exp.start()

        result_var_mult = t_var_mult_exp.join()

        if result_var_mult[0]:
            return result_var_mult

        self.error()

    def var_exp(self):
        result_var_exp =self.var_expr.run_glc()

        print(result_var_exp)
        if result_var_exp[0]:
            return result_var_exp

        self.error()

