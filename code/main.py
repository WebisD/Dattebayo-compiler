import sys
from Compiler.DattebayoCompiler import DattebayoCompiler
""" 

Calls the function that instantiates a compiler
        
"""


class Main:
    def __init__(self, dtb_file):
        """ Performs the creation of an object of type Main

        """
        self.checkArgs(dtb_file)
        self.dtb_file = dtb_file
        self.compileFile()

    def checkArgs(self, dtb_file):
        """ Check if the user pass a valid .dtb file

        :param dtb_file: dtb file
        """
        if not dtb_file.lower().endswith('.dtb'):
            print(f"{dtb_file} is not a Dattebayo file")
            sys.exit()

    def compileFile(self):
        """ Compile the .dtb file

        """
        compiler = DattebayoCompiler(self.dtb_file)
        # compiler.print_lexer_output()


""" Calls the function that start the compiler
        
"""
if __name__ == "__main__":

    main = Main(sys.argv[1])
