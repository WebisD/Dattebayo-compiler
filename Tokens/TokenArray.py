from Tokens.Token import Token
from Tokens.TokenEnum import TokenEnum


class TokenArray(object):
    def __init__(self, dict_tokens):
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
        self.dict_tokens['sunagakure'] = Token(TokenEnum.SUNAGAKURE, "sunagakure", "^(sunagakure)$")
        self.dict_tokens['konohagakure'] = Token(TokenEnum.KONOHAGAKURE, "konohagakure", "^(konohagakure)$")
        self.dict_tokens['kumogakure'] = Token(TokenEnum.KUMOGAKURE, "kumogakure", "^(kumogakure)$")
        self.dict_tokens['amegakure'] = Token(TokenEnum.AMEGAKURE, "amegakure", "^(amegakure)$")
