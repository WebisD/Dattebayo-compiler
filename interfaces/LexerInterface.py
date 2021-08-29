import abc

from interfaces import LexerRulesInterface


class LexerInterface(metaclass=abc.ABCMeta):
    """A Lexer interface that will be used for lexer class creation.
    """
    def __init__(self, lexer_rules: LexerRulesInterface):
        self.rules: LexerRulesInterface = lexer_rules

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'analyze_token')
                and callable(subclass.analyze_token)
                or NotImplemented
        )

    @abc.abstractmethod
    def analyze_token(self, input_data: str):
        """Load in the data set"""
        raise NotImplementedError
