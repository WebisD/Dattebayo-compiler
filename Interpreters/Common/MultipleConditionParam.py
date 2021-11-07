from Interpreters.Common.ConditionParam import ConditionParam
from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression

"""
Class for variables declaration without initialization

                        GLC
MultipleConditionParam ⇐ {[ConditionParam , Operator]} , ConditionParam ;

ConditionParam ⇐ (Values , Comparators , Value) ;
"""


class MultipleConditionParam(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        self.val_conditional = ConditionParam(token_index, token_array)

    def run_glc(self):
        try:
            self.eat(te.LPAREN)
            self.val_conditional = ConditionParam(self.token_index, self.tokens)
            self.att_token(self.var_exp_conditional())
            self.eat(te.RPAREN)
            if (self.current_token.type != te.LPAREN):
                self.var_operator()

            if (self.current_token.type != te.RPAREN):
                self.run_glc()

            return [True, self.token_index, f'valid multiple condition']
        except:
            if self.current_token.type == te.RPAREN:
                return [True, self.token_index, f'valid single condition']

            return [False, self.token_index, f'invalid multiple condition']

    def var_exp_conditional(self):
        result_var_conditional = self.val_conditional.run_glc()

        Expression.append_result(result_var_conditional[2])

        if result_var_conditional[0]:
            return result_var_conditional

        self.error()

    def var_operator(self):        
        token = self.current_token

        if token.type == te.KUMOGAKURE:
            self.eat(te.KUMOGAKURE)
        elif token.type == te.AMEGAKURE:
            self.eat(te.AMEGAKURE)
        else:
            self.error()
    
    def att_token(self, result):
        self.current_token = self.tokens[result[1]]
        self.token_index = result[1]
