from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch
from Interpreters.Expression import Expression
from Interpreters.OperationInterpreter import OperationInterpreter
from Interpreters.Common.Values import Values

"""
Class for variables declaration without initialization

                        GLC
VariableInitialization : (VariableType)* IDENTIFIER HAKU Values
VariableType : RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE
Values : Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation
Num : INT | FLOAT
NumOperation : (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ;
StrOperation : STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;
Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;
"""


class MultipleConditionParam(Expression):
    def __init__(self, token_index: int, token_array=None):
        super().__init__(token_index, token_array)
        self.values_interpreter = Values(token_index, token_array)

    def run_glc(self):
        try:
            return [True, self.token_index, f'Variable initialized with {1}']
        except:
            return [False, self.token_index, None]
