from Tokens.Token import Token
from Tokens.TokenEnum import TokenEnum


class TokenArray(object):
    def __init__(self, dict_tokens=None):
        """ Performs the creation of an object of type TokenArray

        :param dict_tokens: Array of tokens
        """
        if dict_tokens is None:
            dict_tokens = {}
        self.dict_tokens = dict_tokens
        self.add_tokens()

    def add_tokens(self):
        """ Added all tokens in array

        """
        self.dict_tokens['ninjutsu'] = Token(TokenEnum.NINJUTSU, "ninjutsu", r"^(ninjutsu)$")
        self.dict_tokens['genjutsu'] = Token(TokenEnum.GENJUTSU, "genjutsu", r"^(genjutsu)$")
        self.dict_tokens['taijutsu'] = Token(TokenEnum.TAIJUTSU, "taijutsu", r"^(taijutsu)$")
        self.dict_tokens['kagebunshin'] = Token(TokenEnum.KAGEBUNSHIN, "kagebunshin", r"^(kagebunshin)$")
        self.dict_tokens['tsukuyomi'] = Token(TokenEnum.TSUKUYOMI, "tsukuyomi", r"^(tsukuyomi)$")
        self.dict_tokens['chakra'] = Token(TokenEnum.CHAKRA, "chakra", "^(chakra)$")
        self.dict_tokens['kamui'] = Token(TokenEnum.KAMUI, "kamui", "^(kamui)$")
        self.dict_tokens['sharingan'] = Token(TokenEnum.SHARINGAN, "sharingan", r"^(sharingan)$")
        self.dict_tokens['rasengan'] = Token(TokenEnum.RASENGAN, "rasengan", r"^(rasengan)$")
        self.dict_tokens['raikiri'] = Token(TokenEnum.RAIKIRI, "raikiri", "^(raikiri)$")
        self.dict_tokens['zetsu'] = Token(TokenEnum.ZETSU, "zetsu", "^(zetsu)$")
        self.dict_tokens['kuchiyose'] = Token(TokenEnum.KUCHIYOSE, "kuchiyose", r"^(kuchiyose)$")
        self.dict_tokens['fuumashuriken'] = Token(TokenEnum.FUUMASHURIKEN, r"fuumashuriken", "^(fuumashuriken)$")
        self.dict_tokens['kunai'] = Token(TokenEnum.KUNAI, "kunai", "^(kunai)$")
        self.dict_tokens['shuriken'] = Token(TokenEnum.SHURIKEN, "shuriken", r"^(shuriken)$")
        self.dict_tokens['katana'] = Token(TokenEnum.KATANA, "katana", "^(katana)$")
        self.dict_tokens['kirigakure'] = Token(TokenEnum.KIRIGAKURE, "kirigakure", r"^(kirigakure)$")
        self.dict_tokens['kumogakure'] = Token(TokenEnum.KUMOGAKURE, "kumogakure", r"^(kumogakure)$")
        self.dict_tokens['amegakure'] = Token(TokenEnum.AMEGAKURE, "amegakure", r"^(amegakure)$")
        self.dict_tokens['lparen'] = Token(TokenEnum.LPAREN, "lparen", r"^\(")
        self.dict_tokens['rparen'] = Token(TokenEnum.RPAREN, "rparen", r"^\)")
        self.dict_tokens['lbrack'] = Token(TokenEnum.LBRACK, "lbrack", r"^\{")
        self.dict_tokens['rbrack'] = Token(TokenEnum.RBRACK, "rbrack", r"^\}")
        self.dict_tokens['haku'] = Token(TokenEnum.HAKU, "haku", r"^(haku)$")
        self.dict_tokens['endpoint'] = Token(TokenEnum.ENDPOINT, "endpoint", r"^\;$")
        self.dict_tokens['integer'] = Token(TokenEnum.INTEGER, "integer", r"^(-|\+)?\d+")
        self.dict_tokens['float'] = Token(TokenEnum.FLOAT, "float", r"^(-|\+)?[0-9]\d*(.\d+)?")
        self.dict_tokens['boolean'] = Token(TokenEnum.BOOLEAN, "boolean", r"^(True|False|0|1)")
        self.dict_tokens['string'] = Token(TokenEnum.STRING, "string", r"^\"[\s\S]*\"")
        self.dict_tokens['gennin'] = Token(TokenEnum.GENNIN, "gennin", r"^(gennin)$")
        self.dict_tokens['junnin'] = Token(TokenEnum.JUNNIN,  "junnin", r"^(junnin)$")
        self.dict_tokens['identifier'] = Token(TokenEnum.IDENTIFIER, "identifier", r"^([a-zA-Z])+(\w)*")
