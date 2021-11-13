from interfaces.LexerRulesInterface import LexerRulesInterface
from domain.Component import Component


class SyntaxParser():
    def __init__(self,
                lexer_rules = None):
        self.lexer_rules = lexer_rules
        self.array_components = []

    @staticmethod
    def extract_component(self, line):
        component = Component()
        component.name = self.extract_name(line[1])
        component.type = self.extract_type(line[0])

        if component.name is not None and component.type is not None:
            self.array_components.append(component)

    @staticmethod
    def extract_type(self, input_data: str):
        #check in array
        if input_data in self.lexer_rules.reserved_words:
            return input_data
        return None

    @staticmethod
    def extract_name(self, input_data: str):
        #check in array
        if input_data in self.array_components:
            return input_data
        return None
