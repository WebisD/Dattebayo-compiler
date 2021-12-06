import copy

from Interpreters.Expression import Expression
from Interpreters.RThread import ThreadWithReturnValue
from Interpreters.Common.MultipleConditionParam import MultipleConditionParam
from Tokens.TokenEnum import TokenEnum as te

from AST.AST import AST
from AST.IfAST import IfAST

"""

GLC

IfDeclaration : NINJUTSU , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK
MultipleConditionParam : {[ConditionParam , Operator]} , ConditionParam
ConditionParam : (Values , Comparators , Value)
Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation

NumOperation : (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}]
Operation : FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA
StrOperation : STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}]
Comparators : KIRIGAKURE
Expression : ExpressionVariable | ConditionExpr | WhileDeclaration | PrintDeclaration
"""


class IfDeclaration(Expression):
    def __init__(self, token_index: int, token_array=None, interpreter=None):
        """ Performs the creation of an object of type IfDeclaration, in 
        addition will create the GLC of MultipleConditionParam

        :param token_index: index of list tokens
        :param token_array: list tokens
        :param interpreter: a copy of interpreter with all GLCs 
    """
        super().__init__(token_index, token_array)
        self.multiple_cond_param = MultipleConditionParam(token_index, token_array)
        self.expression = copy.deepcopy(interpreter)

    def run_glc(self):
        """ Run the GLC of IfDeclaration and will return the node based on BinOp and custom logs.

        """
        try:
            node = self.if_dec_exp()
            return [True, self.token_index, f'valid if declaration', node]
        except Exception as e:
            a = e
            return [False, self.token_index, f'invalid if declaration', None]

    def if_dec_exp(self) -> AST:
        """ Check the GLC of IfDeclaration and return the If AST. In addition, will
        execute the interpreter to check block of codes inside the if

        """
        self.eat(te.NINJUTSU)

        """Condition"""

        self.eat(te.LPAREN)

        result_cond_list = []

        self.multiple_cond_param.token_index = self.token_index
        self.multiple_cond_param.current_token = self.current_token

        t_multiple_cond_param = ThreadWithReturnValue(target=self.multiple_cond_param.run_glc)
        t_multiple_cond_param.start()

        result_multiple_condition_param = t_multiple_cond_param.join()
        Expression.append_result(result_multiple_condition_param[2])

        if result_multiple_condition_param[0]:
            self.token_index = result_multiple_condition_param[1]
            self.current_token = self.tokens[self.token_index]
        else:
            self.error()

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

        self.eat(te.RBRACK)

        node = IfAST(condition=result_multiple_condition_param[3], scope=result_list)

        return node
