import abc
from typing import List, Tuple, Dict


class LexerRulesInterface(metaclass=abc.ABCMeta):
    """A LexerRules interface that will be used for lexer rules class creation.
    """
    def __init__(self):
        self.reserved_words: Dict[str, str] = {}
        self.identifiers: List[str] = []
        self.operators: List[str] = []

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'reserved_words')
                and hasattr(subclass, 'identifiers')
                and hasattr(subclass, 'operators')
                or NotImplemented
        )
