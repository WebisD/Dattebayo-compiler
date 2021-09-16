import sys
from Compiler.DattebayoCompiler import DattebayoCompiler


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


if __name__ == "__main__":
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('dtb_file', help='.dtb file that contains your dattebayo code')
    args = ap.parse_args()

    main = Main(args.dtb_file)
