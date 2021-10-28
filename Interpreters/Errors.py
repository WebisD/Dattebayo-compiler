class NotMatch(Exception):
    def __init__(self, interpreter_type: str = None, message: str = "No match"):
        self.message = message
        super().__init__(self.message)
