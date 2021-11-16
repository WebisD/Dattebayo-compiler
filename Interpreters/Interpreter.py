import copy
import sys
from Interpreters.RThread import ThreadWithReturnValue
# from Interpreters.OperationInterpreter import OperationInterpreter
# import Interpreters.OperationInterpreter
from Interpreters.Common.NumOperation import NumOperation
from Interpreters.Variable.VariableExpression import VariableExpression
from Interpreters.Expression import Expression
from Interpreters.Print.PrintExpression import PrintExpression
from Interpreters.While.WhileDeclaration import WhileDeclaration
from Interpreters.Conditional.ConditionalExpression import ConditionalExpression
from colorama import Fore, Style
from Tokens.TokenEnum import TokenEnum as te

class Interpreter(Expression):
    def __init__(self, lexer, token_array=None):
        self.token_index = 0

        super().__init__(self.token_index, token_array)

        self.lexer = lexer

        # Interpreters
        self.expression = Expression(self.token_index, self.tokens)
        self.operationInterpreter = NumOperation(self.token_index, self.tokens)
        self.variableInterpreter = VariableExpression(self.token_index, self.tokens)
        self.whileInterpreter = WhileDeclaration(self.token_index, self.tokens)
        self.printInterpreter = PrintExpression(self.token_index, self.tokens)
        self.conditionalInterpreter = ConditionalExpression(self.token_index, self.tokens)

    def error(self):
        raise Exception('Invalid syntax')

    def parser(self):
        try:
            interpreterCopy = copy.deepcopy(self)
            # Expression.decrease_indent()

            while self.token_index < len(self.tokens)-1:
                # print(f"token: {self.token_index}")

                self.operationInterpreter = NumOperation(self.token_index, self.tokens)
                self.variableInterpreter = VariableExpression(self.token_index, self.tokens)
                self.whileInterpreter = WhileDeclaration(self.token_index, self.tokens, interpreterCopy)
                self.printInterpreter = PrintExpression(self.token_index, self.tokens)
                self.conditionalInterpreter = ConditionalExpression(self.token_index, self.tokens, interpreterCopy)

                t_op = ThreadWithReturnValue(target=self.operationInterpreter.run_glc)
                t_var_exp = ThreadWithReturnValue(target=self.variableInterpreter.run_glc)
                t_while_exp = ThreadWithReturnValue(target=self.whileInterpreter.run_glc)
                t_print_exp = ThreadWithReturnValue(target=self.printInterpreter.run_glc)
                t_conditional_exp = ThreadWithReturnValue(target=self.conditionalInterpreter.run_glc)

                list_threads = [
                    t_var_exp,
                    t_conditional_exp,
                    t_print_exp,
                    t_while_exp,
                    t_op
                ]

                for thread in list_threads:
                    thread.start()

                results = []

                Expression.decrease_indent()
                for thread in list_threads:
                    results.append(thread.join())

                errors = 0

                for result in results:
                    Expression.append_result(result[2])
                    if result[0]:
                        self.marker_index = result[1]
                        self.update_interpreter_params()
                        print(f"It's a {result[2]}")
                    else:
                        errors +=1

                if errors == len(list_threads):
                    if self.tokens[self.token_index].type == te.RBRACK:
                        self.eat(te.RBRACK)
                        Expression.decrease_indent()
                    else:
                        raise Exception(f'Could not interpret anything. Current token: {self.tokens[self.token_index]}')
                # return [True, self.token_index, None]

        except Exception as e:
            print(Fore.RED)
            # traceback.print_exc()
            print(e)
            print(Style.RESET_ALL)
            return [False, self.token_index, 'invalid expression']

        return [True, self.token_index, 'valid expression']
