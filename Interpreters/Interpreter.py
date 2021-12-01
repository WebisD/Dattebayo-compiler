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

from AST.AST import AST


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

        self.interpreterCopy = None

    def error(self):
        raise Exception('Invalid syntax')

    def parser(self):
        try:
            self.interpreterCopy = copy.deepcopy(self)

            while self.token_index < len(self.tokens) - 1:
                result = self.run_parser()
                AST.all_ast.append(result[3])

        except Exception as e:
            print('Error:', e)

        return AST.all_ast

    def run_parser(self):
        self.interpreterCopy = copy.deepcopy(self)
        #self.operationInterpreter = NumOperation(self.token_index, self.tokens)
        self.variableInterpreter = VariableExpression(self.token_index, self.tokens)
        self.whileInterpreter = WhileDeclaration(self.token_index, self.tokens, self.interpreterCopy)
        self.printInterpreter = PrintExpression(self.token_index, self.tokens)
        self.conditionalInterpreter = ConditionalExpression(self.token_index, self.tokens, self.interpreterCopy)

        #t_op = ThreadWithReturnValue(target=self.operationInterpreter.run_glc)
        t_var_exp = ThreadWithReturnValue(target=self.variableInterpreter.run_glc)
        t_while_exp = ThreadWithReturnValue(target=self.whileInterpreter.run_glc)
        t_print_exp = ThreadWithReturnValue(target=self.printInterpreter.run_glc)
        t_conditional_exp = ThreadWithReturnValue(target=self.conditionalInterpreter.run_glc)

        list_threads = [
            t_var_exp,
            t_conditional_exp,
            t_print_exp,
            t_while_exp,
            #t_op
        ]

        for thread in list_threads:
            thread.start()

        results = []

        for thread in list_threads:
            results.append(thread.join())

        for result in results:
            Expression.append_result(result[2])
            if result[0]:
                self.marker_index = result[1]
                self.update_interpreter_params()
                return [True, self.token_index, result[2], result[3]]

        self.error()
