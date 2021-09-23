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
            for word in line.split():
                self.get_input(word)
                try:
                    tokens = self.get_next_token()
                    output.extend(tokens)
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

    def check_word(self, pattern: str, text: str) -> Optional[Match[str]]:
        return re.match(pattern, text)

    def replace_word(self, pattern: str, replacement:str, target: str):
        return re.sub(pattern, replacement, target)

    def get_next_token(self) -> List[Token]:
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
