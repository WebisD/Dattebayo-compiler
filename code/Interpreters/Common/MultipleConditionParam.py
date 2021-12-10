from Interpreters.Common.ConditionParam import ConditionParam
from Tokens.TokenEnum import TokenEnum as te
from Interpreters.Expression import Expression

from AST.BinOp import BinOp

"""
Class for variables declaration without initialization

                        GLC
MultipleConditionParam ⇐ {[ConditionParam , Operator]} , ConditionParam ;

ConditionParam ⇐ (Values , Comparators , Value) ;
"""


class MultipleConditionParam(Expression):
    def __init__(self, token_index: int, token_array=None):
        """ Performs the creation of an object of type MultipleConditionParam, in addition
        will create the classes that will interpret the ConditionParam GLC

        :param token_index: index of list tokens
        :param token_array: list tokens
        """
        super().__init__(token_index, token_array)
        self.val_conditional = ConditionParam(token_index, token_array)

    def run_glc(self):
        """ Run the GLC of MultipleConditionParam and will return the node based on BinOp and custom logs.

        """
        try:
            node = self.single_condition_param()[3]

            while self.current_token.type in (te.KUMOGAKURE, te.AMEGAKURE):
                operation = self.var_operator()
                node = BinOp(left=node, op=operation, right=self.single_condition_param()[3])

            return [True, self.token_index, f'valid multiple condition', node]
        except Exception as e:
            a = e
            return [False, self.token_index, f'invalid multiple condition', None]

    def single_condition_param(self):
        """ Run the GLC of ConditionParam and check if it's necessary call again when they are multiple conditions.

        """
        noLparen = False
        try:
            self.eat(te.LPAREN)
        except:
            noLparen = True

        self.val_conditional = ConditionParam(self.token_index, self.tokens)

        result = self.var_exp_conditional()

        self.att_token(result)

        if not noLparen:
            self.eat(te.RPAREN)

        return result

    def var_exp_conditional(self):
        """ Will run the GLC of ConditionParam and will return the result to another function.

        """
        result_var_conditional = self.val_conditional.run_glc()

        Expression.append_result(result_var_conditional[2])

        if result_var_conditional[0]:
            return result_var_conditional

        self.error()

    def var_operator(self):
        """ Will check the operator of conditional based on GLC

        """   
        token = self.current_token

        if token.type == te.KUMOGAKURE:
            self.eat(te.KUMOGAKURE)
        elif token.type == te.AMEGAKURE:
            self.eat(te.AMEGAKURE)
        else:
            self.error()

        return token
    
    def att_token(self, result):
        """ Will atualize the list tokens and token index after execute another GLC

        """
        self.current_token = self.tokens[result[1]]
        self.token_index = result[1]
