class Token(object):
    def __init__(self, type, value, regex=None):
        """ Performs the creation of an object of type Token

        :param type: Type of the token
        :param value: Value of the token
        :param regex: Regex of the token        
        """
        self.type = type
        self.value = value
        self.regex = regex

    def __str__(self):
        """ Custom log

        """
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value), regex=repr(self.regex))

    def __repr__(self):
        return self.__str__()
