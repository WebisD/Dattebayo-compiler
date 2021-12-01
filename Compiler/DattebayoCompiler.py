from typing import TextIO

from Interpreters.Expression import Expression
from Lexer.Lexer import Lexer
from Interpreters.Interpreter import Interpreter
from Visitor.InterpreterVisitor import InterpreterVisitor


class DattebayoCompiler:
    def __init__(self, file=""):
        self.lexer = Lexer()
        self.interpreter = None
        self.lexer_output = None
        self.code_file: TextIO or None = None
        self.read_file(file)
        self.check_code()
        self.close_file()
        self.file_name = None

    def read_file(self, file):
        self.file_name = file
        self.code_file = open(file, "r")

    def close_file(self):
        self.code_file.close()

    def check_code(self):
        self.check_lexer(self.code_file)
        self.check_syntax(self.code_file)
        #Expression.print_logs()

    def check_lexer(self, line):
        self.log(self.__class__, self.check_lexer, "start")
        self.lexer_output = self.lexer.run_lexer(self.code_file)
        # self.print_lexer_output()
        self.log(self.__class__, self.check_lexer, "end")

    def check_syntax(self, line):
        self.log(self.__class__, self.check_syntax, "start")
        self.interpreter = Interpreter(self.lexer, self.lexer_output)
        result = self.interpreter.parser()
        print(len(result))
        visitor = InterpreterVisitor(result, self.file_name)
        code = visitor.run_visitor()
        print(code)
        # print(result)
        self.log(self.__class__, self.check_syntax, "end")

    def print_lexer_output(self):
        for token in self.lexer_output:
            print(token)

    def log(self, class_obj, function_obj, msg):
        print(f"\n{class_obj.__name__}/{function_obj.__name__}:{msg}\n")
