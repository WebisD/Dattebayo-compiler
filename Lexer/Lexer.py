import re
from typing import Optional, Match, List, Any
from typing.io import TextIO
from Tokens.TokenArray import TokenArray
from Tokens.Token import Token


class Lexer:
    def __init__(self):
        self.token_array = TokenArray()
        self.current_text: str or None = None
        self.is_reading: bool = False

    def run_lexer(self, code: TextIO) -> List[Any]:
        output: List[Any] = []

        for line in code.readlines():
            for word in line.split(" "):
                self.get_input(word)
                try:
                    output.append(self.get_next_token())
                except Exception as e:
                    output.append(e)

                self.finish()

        return output

    def get_input(self, text):
        self.current_text = text
        self.is_reading = True

    def finish(self):
        self.current_text: str or None = None
        self.is_reading: bool = False

    def check_word(self, pattern:str, text: str) -> Optional[Match[str]]:
        return re.fullmatch(pattern, text)

    def get_next_token(self):
        if not self.is_reading:
            return False

        token = None

        for k, v in self.token_array.dict_tokens.items():
            if self.check_word(self.token_array.dict_tokens[k].regex, self.current_text):
                token = self.token_array.dict_tokens[k]
                break

        if token is None:
            self.error(self.current_text)

        return token

    def error(self, text):
        raise Exception(f"Invalid token: {text}")
