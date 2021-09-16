class DattebayoCompiler:
    def __init__(self, file=""):
        self.code = None
        self.read_file(file)
        self.check_code()

    def read_file(self, file):
        with open(file, "r") as code:
            self.code = code

    def check_code(self):
        self.check_lexer(self.code)
        self.check_syntax(self.code)

    def check_lexer(self, line):
        pass

    def check_syntax(self, line):
        pass
