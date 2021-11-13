import sys
from Compiler.DattebayoCompiler import DattebayoCompiler

""" Calls the function that instantiates a compiler
        
"""
class Main:
    def __init__(self, dtb_file):
        self.checkArgs(dtb_file)
        self.dtb_file = dtb_file
        print(self.dtb_file)
        self.compileFile()

    def checkArgs(self, dtb_file):
        if not dtb_file.lower().endswith('.dtb'):
            print(f"{dtb_file} is not a Dattebayo file")
            sys.exit()

    def compileFile(self):
        compiler = DattebayoCompiler(self.dtb_file)
        # compiler.print_lexer_output()


if __name__ == "__main__":

    main = Main(sys.argv[1])
