from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
import Interpreters.OperationInterpreter as OpeI
from Lexer.Lexer import Lexer
from Interpreters.RThread import ThreadWithReturnValue
#from Interpreters.OperationInterpreter import OperationInterpreter
import Interpreters.OperationInterpreter


class Interpreter:
    def __init__(self, lexer, token_array=None):
        if token_array is None:
            token_array = []

        self.tokens = token_array
        self.lexer = lexer
        # self.current_token = self.lexer.get_next_token()
        self.token_index = 0
        self.operationInterpreter = None

    def error(self):
        raise Exception('Invalid syntax')

    def parser(self):
        try:
            self.operationInterpreter = Interpreters.OperationInterpreter.OperationInterpreter(self.token_index, self.tokens)
            tOp = ThreadWithReturnValue(target=self.operationInterpreter.run_glc)

            tOp.start()

            resultOp = tOp.join()

            # Itś an Operation
            if resultOp[0]:
                print("It's a operation")

                return resultOp[2]

        except Exception as e:
            print(e)
