from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Variable.VariableExpression import VariableExpression
from Interpreters.Common.ConditionParam import ConditionParam
from Interpreters.Common.MultipleConditionParam import MultipleConditionParam
from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression


from AST.WhileAST import WhileAST
"""
Class for variables declaration of while loop

                        GLC

WhileDeclaration ⇐ TSUKUYOMI , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

"""


class WhileDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        """ Performs the creation of an object of type WhileDeclaration, in addition
        will create the classes that will interpret the VariableExpression and MultipleConditionParam GLC

        :param token_index: index of list tokens
        :param token_array: list tokens
        :param interpreter: a copy of interpreter with all GLCs 
        """
        super().__init__(token_index, token_array)
        self.var_multiple = MultipleConditionParam(token_index, token_array)
        self.var_expr = VariableExpression(token_index, token_array)
        self.expression = interpreter

    def run_glc(self):
        """ Run the GLC of WhileDeclaration and will return the node based on BinOp and custom logs.
        In addition, will execute the interpreter to check block of codes inside the while

        """
        try:
            self.eat(te.TSUKUYOMI)
            self.eat(te.LPAREN)

            cond = self.conditions()

            self.eat(te.RPAREN)

            """Scope // Code inside if statement"""

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

            # self.att_token(self.var_exp())
            self.eat(te.RBRACK)

            node = WhileAST(condition=cond[3], scope=result_list)

            return [True, self.token_index, f'valid while expression', node]
        except:
            return [False, self.token_index, 'invalid while expression', None]

    def conditions(self):
        """ Run the GLC of MultipleConditionParam or ConditionParam and return the result.

        """
        if self.current_token.type == te.LPAREN:
            self.var_multiple = MultipleConditionParam(self.token_index, self.tokens)
        else:
            self.var_multiple = ConditionParam(self.token_index, self.tokens)

        result = self.var_conditional()
        self.att_token(result)

        return result

    def var_conditional(self):
        """ Run the GLC of Conditional and return the result.

        """
        result_var_mult = self.var_multiple.run_glc()

        Expression.append_result(result_var_mult[2])

        if result_var_mult[0]:
            return result_var_mult

        self.error()

    def att_token(self, result):
        """ Will atualize the list tokens and token index after execute another GLC

        """
        self.current_token = self.tokens[result[1]]
        self.token_index = result[1]
