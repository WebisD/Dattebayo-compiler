class SymbolTable:
    """ Class for Symbols tables """

    symbol_table = {}

    def __init__(self) -> None:
        """ Performs the creation of an object of type SymbolTable

        """
        pass
    
    @staticmethod
    def get_varaible(variable):
        """ Get the variable and check in SymbolTable if already exists

        """
        type = variable[1]
        name = SymbolTable.check_name(variable[0])

        if not name:
            print("Already exists")

    def check_name(name):
        """ Get the name of variable and check in SymbolTable if already exists

        """
        if name in SymbolTable.symbol_table:
            return None

