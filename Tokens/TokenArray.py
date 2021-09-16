from Tokens.Token import Token
from Tokens.TokenEnum import TokenEnum


class TokenArray(object):
  def __init__(self, array_tokens):
    self.array_tokens = array_tokens
    self.add_tokens()

  def add_tokens(self):
    ninjutsu = Token(TokenEnum.NINJUTSU, "ninjutsu", "^(ninjutsu)$")
    genjutsu = Token(TokenEnum.GENJUTSU, "genjutsu", "^(genjutsu)$")
    taijutsu = Token(TokenEnum.TAIJUTSU, "taijutsu", "^(taijutsu)$")

    self.array_tokens.append(ninjutsu)
    self.array_tokens.append(genjutsu)
    self.array_tokens.append(taijutsu)

