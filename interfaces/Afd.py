import abc

from interfaces import LexerRulesInterface


class Afd(metaclass=abc.ABCMeta):
    """skdjalkdj
    """
    def __init__(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'handle')
                and callable(subclass.handle)
                or NotImplemented
        )

    @abc.abstractmethod
    def handle(self, input_data: str):
        """Handle input"""
        raise NotImplementedError
