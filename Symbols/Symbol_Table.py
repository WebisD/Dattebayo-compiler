"""
Integrantes:

Nome: Antônio Gustavo Muniz           22.119.001-0 
Nome: João Vitor Dias dos Santos 	  22.119.006-9 
Nome: Weverson da Silva Pereira       22.119.004-4

"""
import json
from Symbol import Symbol


class SymbolTable:
    """ Class for Symbols tables """

    symbol_table = {}

    def __init__(self) -> None:
        pass

    @staticmethod
    def set_varaible(kw_symbol):
        SymbolTable.symbol_table[kw_symbol.name] = {"name": kw_symbol.name, "type": kw_symbol.type,
                                                    "scope": kw_symbol.scope}

    @staticmethod
    def get_symbol_table():
        return SymbolTable.symbol_table

    def __str__(self):
        return json.dumps(SymbolTable.symbol_table, indent=4)
