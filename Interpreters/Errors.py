class NotMatch(Exception):
    def __init__(self, message: str = "No match"):
        self.message = message
        super().__init__(self.message)
