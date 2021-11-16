from Tokens.Token import Token
from Tokens.TokenEnum import TokenEnum as te


class TokenArray(object):
    def __init__(self, dict_tokens=None):
        if dict_tokens is None:
            dict_tokens = {}
        self.dict_tokens = dict_tokens
        self.operators: list = [te.FUUMASHURIKEN, te.KUNAI, te.SHURIKEN, te.KATANA,te.HAKU, te.KIRIGAKURE, te.KUMOGAKURE, te.AMEGAKURE, te.JUNNIN, te.GENNIN]
        self.user_defined: list = [te.INTEGER, te.FLOAT, te.BOOLEAN, te.STRING, te.IDENTIFIER]
        self.conditions: list = [te.NINJUTSU, te.GENJUTSU, te.TAIJUTSU]
        self.loop: list = [te.KAGEBUNSHIN, te.TSUKUYOMI]
        self.types: list = [te.RASENGAN, te.RAIKIRI, te.ZETSU, te.KUCHIYOSE]
        self.add_tokens()

    def add_tokens(self):
        self.dict_tokens['ninjutsu'] = Token(te.NINJUTSU, "ninjutsu", r"^(ninjutsu)$")
        self.dict_tokens['genjutsu'] = Token(te.GENJUTSU, "genjutsu", r"^(genjutsu)$")
        self.dict_tokens['taijutsu'] = Token(te.TAIJUTSU, "taijutsu", r"^(taijutsu)$")
        self.dict_tokens['kagebunshin'] = Token(te.KAGEBUNSHIN, "kagebunshin", r"^(kagebunshin)$")
        self.dict_tokens['tsukuyomi'] = Token(te.TSUKUYOMI, "tsukuyomi", r"^(tsukuyomi)$")
        self.dict_tokens['chakra'] = Token(te.CHAKRA, "chakra", "^(chakra)$")
        self.dict_tokens['kamui'] = Token(te.KAMUI, "kamui", "^(kamui)$")
        self.dict_tokens['sharingan'] = Token(te.SHARINGAN, "sharingan", r"^(sharingan)$")
        self.dict_tokens['rasengan'] = Token(te.RASENGAN, "rasengan", r"^(rasengan)$")
        self.dict_tokens['raikiri'] = Token(te.RAIKIRI, "raikiri", "^(raikiri)$")
        self.dict_tokens['zetsu'] = Token(te.ZETSU, "zetsu", "^(zetsu)$")
        self.dict_tokens['kuchiyose'] = Token(te.KUCHIYOSE, "kuchiyose", r"^(kuchiyose)$")
        self.dict_tokens['fuumashuriken'] = Token(te.FUUMASHURIKEN, r"fuumashuriken", "^(fuumashuriken)$")
        self.dict_tokens['kunai'] = Token(te.KUNAI, "kunai", "^(kunai)$")
        self.dict_tokens['shuriken'] = Token(te.SHURIKEN, "shuriken", r"^(shuriken)$")
        self.dict_tokens['katana'] = Token(te.KATANA, "katana", "^(katana)$")
        self.dict_tokens['kirigakure'] = Token(te.KIRIGAKURE, "kirigakure", r"^(kirigakure)$")
        self.dict_tokens['kumogakure'] = Token(te.KUMOGAKURE, "kumogakure", r"^(kumogakure)$")
        self.dict_tokens['amegakure'] = Token(te.AMEGAKURE, "amegakure", r"^(amegakure)$")
        self.dict_tokens['lparen'] = Token(te.LPAREN, "lparen", r"^\(")
        self.dict_tokens['rparen'] = Token(te.RPAREN, "rparen", r"^\)")
        self.dict_tokens['lbrack'] = Token(te.LBRACK, "lbrack", r"^\{")
        self.dict_tokens['rbrack'] = Token(te.RBRACK, "rbrack", r"^\}")
        self.dict_tokens['haku'] = Token(te.HAKU, "haku", r"^(haku)$")
        self.dict_tokens['endpoint'] = Token(te.ENDPOINT, "endpoint", r"^\;$")
        self.dict_tokens['integer'] = Token(te.INTEGER, "integer", r"^(-|\+)?\d+")
        self.dict_tokens['float'] = Token(te.FLOAT, "float", r"^(-|\+)?[0-9]\d*(.\d+)?")
        self.dict_tokens['boolean'] = Token(te.BOOLEAN, "boolean", r"^(True|False|0|1)")
        self.dict_tokens['string'] = Token(te.STRING, "string", r"^\"[\s\S]*\"")
        self.dict_tokens['gennin'] = Token(te.GENNIN, "gennin", r"^(gennin)$")
        self.dict_tokens['junnin'] = Token(te.JUNNIN,  "junnin", r"^(junnin)$")
        self.dict_tokens['identifier'] = Token(te.IDENTIFIER, "identifier", r"^([a-zA-Z])+(\w)*")
