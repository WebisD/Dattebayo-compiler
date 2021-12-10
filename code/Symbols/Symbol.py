class Symbol:
    def __init__(self, type, name, scope):
        """ Performs the creation of an object of type Symbol

        :param type: Type of the Symbol
        :param name: name of the Symbol
        :param scope: scope of the Symbol        
        """
        self.type = type
        self.name = name
        self.scope = scope

    # ToDo: Check variables
    