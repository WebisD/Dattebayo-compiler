from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression
from Interpreters.Variable.VariableDeclaration import VariableDeclaration
from Interpreters.Variable.VariableInitialization import VariableInitialization
from Interpreters.RThread import ThreadWithReturnValue

"""

                                    GLC
VariableExpression : (VariableDeclaration | VariableInitialization) ENDPOINT
VariableDeclaration : VariableType IDENTIFIER
VariableInitialization : (VariableType)* IDENTIFIER HAKU Values
VariableType : RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE
Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation
Num : INT | FLOAT
NumOperation : (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ;
StrOperation : STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;
Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;
"""


class VariableExpression(Expression):
    def __init__(self, token_index: int, token_array=None):
        """ Performs the creation of an object of type VariableExpression, in addition
        will create the classes that will interpret the VariableDeclaration and VariableInitialization GLC

        :param token_index: index of list tokens
        :param token_array: list tokens
        :param interpreter: a copy of interpreter with all GLCs 
        """
        super().__init__(token_index, token_array)
        self.var_dec = VariableDeclaration(token_index, token_array)
        self.var_ini = VariableInitialization(token_index, token_array)

    def run_glc(self):
        """ Run the GLC of VariableExpression and will return the node based on BinOp and custom logs.

        """
        try:
            result = self.var_exp()
            return [True, result[1], f'valid variable expression {result[2]}', result[3]]
        except:
            return [False, self.token_index, 'invalid variable expression', None]

    def var_exp(self):
        """ Run the GLC of VariableDeclaration and VariableInitialization and return the result.

        """
        t_var_dec = ThreadWithReturnValue(target=self.var_dec.run_glc)
        t_var_ini = ThreadWithReturnValue(target=self.var_ini.run_glc)

        t_var_dec.start()
        t_var_ini.start()

        result_var_dec = t_var_dec.join()
        result_var_inc = t_var_ini.join()

        if result_var_dec[0]:
            return result_var_dec
        elif result_var_inc[0]:
            return result_var_inc

        self.error()
