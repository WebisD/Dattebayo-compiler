import re
from typing import Optional, Match, List, Any
from Tokens.TokenEnum import TokenEnum
from typing.io import TextIO
from Tokens.TokenArray import TokenArray
from Tokens.Token import Token

"""
                Lexer

Check if the words (tokens) are correct
"""


class Lexer:
    def __init__(self):
        self.token_array = TokenArray()
        self.current_text: str or None = None
        self.is_reading: bool = False

        self.all_tokens: List[Token] or None = None
        self.index_tokens = 0
        self.current_token = None

        self.pattern_split_semicolon = ''';(?=(?:"[^"]*")*$)'''
        self.pattern_split_text = '''\s+(?=(?:[^"]|"[^"]*")*$)'''

    def run_lexer(self, code: TextIO) -> List[Any]:
        self.all_tokens: List[Any] = []

        for line in code.readlines():
            space_semicolon = re.sub(self.pattern_split_semicolon, ' ;', line)
            splited_line = re.split(self.pattern_split_text, space_semicolon)
            splited_line = list(filter(''.__ne__, splited_line))
            for word in splited_line:
                self.get_input(word)
                try:
                    tokens = self.get_tokens()
                    self.all_tokens.extend(tokens)
                except Exception as e:
                    self.all_tokens.append(e)

                self.finish()

        return self.all_tokens

    def get_input(self, text):
        self.current_text = text
        self.is_reading = True

    def finish(self):
        self.current_text: str or None = None
        self.is_reading: bool = False

    def check_word(self, pattern: str, text: str) -> Optional[Match[str]]:
        match = re.match(pattern, text, re.MULTILINE)
        return match

    def replace_word(self, pattern: str, replacement: str, target: str):
        return re.sub(pattern, replacement, target)

    def find_longest_match(self):
        max_match = [0, None]
        k_index = -1

        for k, v in self.token_array.dict_tokens.items():
            match = self.check_word(v.regex, self.current_text)
            if match:
                num_match = match.end() - match.start()
                if num_match > max_match[0]:
                    max_match = [num_match, match]
                    k_index = k

        return max_match[1], k_index

    def get_tokens(self) -> List[Token]:
        if not self.is_reading:
            return []

        error = False

        tokens = []

        while self.current_text != "" and not error:
            continue_loop = False
            # print(f"current text: {self.current_text}")

            match, k = self.find_longest_match()
            if match:
                aaa = match[0]
                # print(f"\tinside if: {self.token_array.dict_tokens[k].type}")
                if self.token_array.dict_tokens[k].type == TokenEnum.INTEGER:
                    tokens.append(Token(self.token_array.dict_tokens[k].type, int(match[0])))
                elif self.token_array.dict_tokens[k].type == TokenEnum.FLOAT:
                    tokens.append(Token(self.token_array.dict_tokens[k].type, float(match[0])))
                else:
                    tokens.append(Token(self.token_array.dict_tokens[k].type, match[0]))
                self.current_text = self.replace_word(self.token_array.dict_tokens[k].regex, '', self.current_text)
                continue_loop = True

            if continue_loop:
                continue

            error = True

        if len(tokens) == 0 or error:
            self.error(self.current_text)

        return tokens

    def error(self, text):
        raise Exception(f"Invalid token: {text}")
