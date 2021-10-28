from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
import Interpreters.OperationInterpreter as OpeI
from Lexer.Lexer import Lexer
from Interpreters.OperationInterpreter import OperationInterpreter


class Interpreter:
    def __init__(self, lexer, token_array=None):
        if token_array is None:
            token_array = []

        self.tokens = token_array
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

        self.operationInterpreter = None

    def error(self):
        raise Exception('Invalid syntax')

    def parser(self):
        try:
            self.operationInterpreter = OperationInterpreter(self.lexer, self.lexer)
            print('oi')
            #self.operation_interpreter.expr()
        except Exception as e:
            print(e)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            try:
                self.current_token = next(self.tokens)
            except StopIteration as e:
                pass
            except Exception as e:
                print(f"Error {self.current_token}")
        else:
            self.error()
