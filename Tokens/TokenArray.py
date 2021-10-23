from Tokens.Token import Token
from Tokens.TokenEnum import TokenEnum


class TokenArray(object):
    def __init__(self, dict_tokens=None):
        if dict_tokens is None:
            dict_tokens = {}
        self.dict_tokens = dict_tokens
        self.add_tokens()

    def add_tokens(self):
        self.dict_tokens['ninjutsu'] = Token(TokenEnum.NINJUTSU, "ninjutsu", "^(ninjutsu)$")
        self.dict_tokens['genjutsu'] = Token(TokenEnum.GENJUTSU, "genjutsu", "^(genjutsu)$")
        self.dict_tokens['taijutsu'] = Token(TokenEnum.TAIJUTSU, "taijutsu", "^(taijutsu)$")
        self.dict_tokens['kagebunshin'] = Token(TokenEnum.KAGEBUNSHIN, "kagebunshin", "^(kagebunshin)$")
        self.dict_tokens['tsukuyomi'] = Token(TokenEnum.TSUKUYOMI, "tsukuyomi", "^(tsukuyomi)$")
        self.dict_tokens['chakra'] = Token(TokenEnum.CHAKRA, "chakra", "^(chakra)$")
        self.dict_tokens['kamui'] = Token(TokenEnum.KAMUI, "kamui", "^(kamui)$")
        self.dict_tokens['sharingan'] = Token(TokenEnum.SHARINGAN, "sharingan", "^(sharingan)$")
        self.dict_tokens['rasengan'] = Token(TokenEnum.RASENGAN, "rasengan", "^(rasengan)$")
        self.dict_tokens['raikiri'] = Token(TokenEnum.RAIKIRI, "raikiri", "^(raikiri)$")
        self.dict_tokens['zetsu'] = Token(TokenEnum.ZETSU, "zetsu", "^(zetsu)$")
        self.dict_tokens['kuchiyose'] = Token(TokenEnum.KUCHIYOSE, "kuchiyose", "^(kuchiyose)$")
        self.dict_tokens['fuumashuriken'] = Token(TokenEnum.FUUMASHURIKEN, "fuumashuriken", "^(fuumashuriken)$")
        self.dict_tokens['kunai'] = Token(TokenEnum.KUNAI, "kunai", "^(kunai)$")
        self.dict_tokens['shuriken'] = Token(TokenEnum.SHURIKEN, "shuriken", "^(shuriken)$")
        self.dict_tokens['katana'] = Token(TokenEnum.KATANA, "katana", "^(katana)$")
        self.dict_tokens['kirigakure'] = Token(TokenEnum.KIRIGAKURE, "kirigakure", "^(kirigakure)$")
        self.dict_tokens['kumogakure'] = Token(TokenEnum.KUMOGAKURE, "kumogakure", "^(kumogakure)$")
        self.dict_tokens['amegakure'] = Token(TokenEnum.AMEGAKURE, "amegakure", "^(amegakure)$")
        self.dict_tokens['lparen'] = Token(TokenEnum.LPAREN, "lparen", "^\(")
        self.dict_tokens['rparen'] = Token(TokenEnum.RPAREN, "rparen", "^\)")
        self.dict_tokens['lbrack'] = Token(TokenEnum.LBRACK, "lbrack", "^\{")
        self.dict_tokens['rbrack'] = Token(TokenEnum.RBRACK, "rbrack", "^\}")
        self.dict_tokens['haku'] = Token(TokenEnum.HAKU, "haku", "^(haku)$")
        self.dict_tokens['endpoint'] = Token(TokenEnum.ENDPOINT, "endpoint", "^\;$")
        self.dict_tokens['integer'] = Token(TokenEnum.INTEGER, "integer", "^(-|\+)?\d+")
        self.dict_tokens['float'] = Token(TokenEnum.FLOAT, "float", "^(-|\+)?[0-9]\d*(.\d+)?")
        self.dict_tokens['boolean'] = Token(TokenEnum.BOOLEAN, "boolean", "^(True|False|0|1)")
        self.dict_tokens['string'] = Token(TokenEnum.STRING, "string", "^\"[\s\S]*\"")
        self.dict_tokens['identifier'] = Token(TokenEnum.IDENTIFIER, "identifier", "^([a-zA-Z])+(\w)*")