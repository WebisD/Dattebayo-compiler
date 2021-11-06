from Interpreters.While.WhileDeclaration import WhileDeclaration
from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
import Interpreters.OperationInterpreter as OpeI
from Lexer.Lexer import Lexer
from Interpreters.RThread import ThreadWithReturnValue
# from Interpreters.OperationInterpreter import OperationInterpreter
# import Interpreters.OperationInterpreter
from Interpreters.OperationInterpreter import OperationInterpreter
from Interpreters.Variable.VariableExpression import VariableExpression
from Interpreters.Expression import Expression


class Interpreter(Expression):
    def __init__(self, lexer, token_array=None):
        self.token_index = 0

        super().__init__(self.token_index, token_array)

        self.lexer = lexer

        # Interpreters
        self.expression = Expression(self.token_index, self.tokens)
        self.operationInterpreter = OperationInterpreter(self.token_index, self.tokens)
        self.variableInterpreter = VariableExpression(self.token_index, self.tokens)
        self.whileInterpreter = WhileDeclaration(self.token_index, self.tokens)

    def error(self):
        raise Exception('Invalid syntax')

    def parser(self):
        try:

            while self.token_index < len(self.tokens):
                self.operationInterpreter = OperationInterpreter(self.token_index, self.tokens)
                self.variableInterpreter = VariableExpression(self.token_index, self.tokens)
                self.whileInterpreter = WhileDeclaration(self.token_index, self.tokens)

                t_op = ThreadWithReturnValue(target=self.operationInterpreter.run_glc)
                t_var_exp = ThreadWithReturnValue(target=self.variableInterpreter.run_glc)
                t_while_exp = ThreadWithReturnValue(target=self.whileInterpreter.run_glc)

                list_threads = [t_var_exp, t_op, t_while_exp]

                for thread in list_threads:
                    thread.start()

                results = []

                for thread in list_threads:
                    results.append(thread.join())

                for result in results:
                    if result[0]:
                        self.marker_index = result[1]
                        self.update_interpreter_params()
                        print(f"It's a {result[2]}")
                    #print('---', result)

        except Exception as e:
            print('deu merda', e)
