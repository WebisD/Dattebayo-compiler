from typing import TextIO

from Interpreters.Expression import Expression
from Lexer.Lexer import Lexer
from Interpreters.Interpreter import Interpreter
from Visitor.InterpreterVisitor import InterpreterVisitor


class DattebayoCompiler:
    def __init__(self, file=""):
        """ Performs the creation of an object of type DattebayoCompiler, in addition
        will create the classes that will convert the .dtb file to python code

        :param file: File .dtb to be read
        """
        self.lexer = Lexer()
        self.interpreter = None
        self.lexer_output = None
        self.code_file: TextIO or None = None
        self.read_file(file)
        self.check_code()
        self.close_file()
        self.file_name = None

    def read_file(self, file):
        """ Read .dtb file based on name 

        :param file: File .dtb to be read
        """
        self.file_name = file
        self.code_file = open(file, "r")

    def close_file(self):
        """ Close read file 

        """
        self.code_file.close()

    def check_code(self):
        """ Pass the code file form .dtb to check lexer and syntax  

        """
        self.check_lexer(self.code_file)
        self.check_syntax(self.code_file)
        # Expression.print_logs()

    def check_lexer(self, line):
        """ Apply the lexer in the .dtb code file 

        :param line: each line of .dtb file
        """
        # self.log(self.__class__, self.check_lexer, "start")
        self.lexer_output = self.lexer.run_lexer(self.code_file)
        # self.print_lexer_output()
        # self.log(self.__class__, self.check_lexer, "end")

    def check_syntax(self, line):
        """ Apply the syntax interpreter in the .dtb code file 

        :param line: each line of .dtb file
        """
        # self.log(self.__class__, self.check_syntax, "start")
        self.interpreter = Interpreter(self.lexer, self.lexer_output)
        result = self.interpreter.parser()
        visitor = InterpreterVisitor(result, self.file_name)
        code = visitor.run_visitor()
        # self.log(self.__class__, self.check_syntax, "end")

    def print_lexer_output(self):
        """ Print all tokens read in the Lexer class

        """
        for token in self.lexer_output:
            print(token)

    def log(self, class_obj, function_obj, msg):
        """ Custom log

        :param class_obj: the class object
        :param function_obj: function of this object
        :param msg: the log message

        """
        print(f"\n{class_obj.__name__}/{function_obj.__name__}:{msg}\n")
