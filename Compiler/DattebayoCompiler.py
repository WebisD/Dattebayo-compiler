from typing import TextIO

from Lexer.Lexer import Lexer

class DattebayoCompiler:
    def __init__(self, file=""):
        self.lexer = Lexer()
        self.lexer_output = None
        self.code_file: TextIO or None = None
        self.read_file(file)
        self.check_code()
        self.close_file()

    def read_file(self, file):
        self.code_file = open(file, "r")

    def close_file(self):
        self.code_file.close()

    def check_code(self):
        self.check_lexer(self.code_file)
        self.check_syntax(self.code_file)

    def check_lexer(self, line):
        self.lexer_output = self.lexer.run_lexer(self.code_file)

    def check_syntax(self, line):
        pass

    def print_lexer_output(self):
        for token in self.lexer_output:
            print(token)
