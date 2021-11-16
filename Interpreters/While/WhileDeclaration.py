from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Variable.VariableExpression import VariableExpression
from Interpreters.Common.ConditionParam import ConditionParam
from Interpreters.Common.MultipleConditionParam import MultipleConditionParam
from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression

"""
Class for variables declaration of while loop

                        GLC

WhileDeclaration ⇐ TSUKUYOMI , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

"""


class WhileDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        super().__init__(token_index, token_array)
        self.var_multiple = MultipleConditionParam(token_index, token_array)
        self.var_expr = VariableExpression(token_index, token_array)
        self.expression = interpreter

    def run_glc(self):
        try:
            self.eat(te.TSUKUYOMI)
            self.eat(te.LPAREN)
            
            if self.current_token.type == te.LPAREN:
                self.var_multiple = MultipleConditionParam(self.token_index, self.tokens)
                self.att_token(self.var_conditional())
            else:
                self.var_multiple = ConditionParam(self.token_index, self.tokens)
                self.att_token(self.var_conditional())

            self.eat(te.RPAREN)
            self.eat(te.LBRACK)

            Expression.increase_indent()

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


            #self.att_token(self.var_exp())
            self.eat(te.RBRACK)

            return [True, self.token_index, f'valid while expression']
        except:
            return [False, self.token_index, 'invalid while expression']

    def var_conditional(self):
        result_var_mult = self.var_multiple.run_glc()

        Expression.append_result(result_var_mult[2])

        if result_var_mult[0]:
            return result_var_mult

        self.error()

    def att_token(self, result):
        self.current_token = self.tokens[result[1]]
        self.token_index = result[1]
