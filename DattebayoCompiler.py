class DattebayoCompiler():
    def __init__(self,
                file= ""):
        self.read_file(file)

    def read_file(self, file):
        with open(file, "r") as file:
            self.validate_code(file.readlines())

    def validate_code(self, lines):
        self.validate_lexer(lines)
        self.validate_syntax(lines)

    def validate_lexer(self, line):
        pass

    def validate_syntax(self, line):
        pass