class Token(object):
  def __init__(self, type, value, regex):
    self.type = type
    self.value = value
    self.regex = regex

  def __str__(self):
    return "Token({type}, {value}, {regex})".format(type = self.type, value = repr(self.value), regex = repr(self.regex))

  def __repr__(self):
    return self.__str__()