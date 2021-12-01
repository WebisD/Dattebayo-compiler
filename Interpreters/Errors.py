class NotMatch(Exception):
    def __init__(self, message: str = "No match"):
        """ Performs the creation of an object of type NotMatch

        :param message: log of error
    """
        self.message = message
        super().__init__(self.message)
