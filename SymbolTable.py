class SymbolTable:
    """ Class for Symbols tables """

    symbol_table = {}

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_varaible(variable):
        type = variable[1]
        name = SymbolTable.check_name(variable[0])

        if not name:
            print("Already exists")

    def check_name(name):
        if name in SymbolTable.symbol_table:
            return None

