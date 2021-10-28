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

    def run_lexer(self, code: TextIO) -> List[Any]:
        self.all_tokens: List[Any] = []

        for line in code.readlines():
            for word in line.split():
                self.get_input(word)
                try:
                    tokens = self.get_tokens()
                    self.all_tokens.extend(tokens)
                except Exception as e:
                    self.all_tokens.append(e)

                self.finish()

        return self.all_tokens

    def get_next_token(self):
        if not self.current_token:
            self.index_tokens = 0

        if self.index_tokens == len(self.all_tokens):
            return None

        self.current_token = self.all_tokens[self.index_tokens]
        self.index_tokens += 1

        return self.current_token

    def get_input(self, text):
        self.current_text = text
        self.is_reading = True

    def finish(self):
        self.current_text: str or None = None
        self.is_reading: bool = False

    def check_word(self, pattern: str, text: str) -> Optional[Match[str]]:
        return re.match(pattern, text)

    def replace_word(self, pattern: str, replacement: str, target: str):
        return re.sub(pattern, replacement, target)

    def get_tokens(self) -> List[Token]:
        if not self.is_reading:
            return []

        error = False

        tokens = []

        while self.current_text != "" and not error:
            continue_loop = False
            # print(f"current text: {self.current_text}")

            for k, v in self.token_array.dict_tokens.items():
                match = self.check_word(self.token_array.dict_tokens[k].regex, self.current_text)
                if match:
                    # print(f"\tinside if: {self.token_array.dict_tokens[k].type}")
                    if self.token_array.dict_tokens[k].type == TokenEnum.INTEGER:
                        tokens.append(Token(self.token_array.dict_tokens[k].type, int(match[0])))
                    elif self.token_array.dict_tokens[k].type == TokenEnum.FLOAT:
                        tokens.append(Token(self.token_array.dict_tokens[k].type, float(match[0])))
                    else:
                        tokens.append(Token(self.token_array.dict_tokens[k].type, match[0]))
                    self.current_text = self.replace_word(self.token_array.dict_tokens[k].regex, '', self.current_text)
                    continue_loop = True
                    break

            if continue_loop:
                continue

            error = True

        if len(tokens) == 0 or error:
            self.error(self.current_text)

        return tokens

    def error(self, text):
        raise Exception(f"Invalid token: {text}")
