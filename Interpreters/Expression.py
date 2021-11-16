from Interpreters.RThread import ThreadWithReturnValue
from Tokens.TokenArray import TokenArray
from Tokens.TokenEnum import TokenEnum as te
from Tokens.Token import Token
from Interpreters.Errors import NotMatch

"""
            Expression
                
Parent class for all interpreters

"""


class Expression:
    #__shared_state = {}

    logs = []
    indentation_level = 0
    output_indexes = []

    def __init__(self, token_index: int, token_array=None):
        if token_array is None:
            token_array = []
        self.tokens = token_array
        self.current_token: Token = token_array[token_index]
        self.token_index = token_index
        self.marker_index = 0
        self.output: str = ""
        self.tokens_list = TokenArray()

    def error(self):
        raise NotMatch

    def update_interpreter_params(self):
        if self.token_index != self.marker_index:
            self.token_index = self.marker_index
            if self.marker_index < len(self.tokens):
                self.current_token: Token = self.tokens[self.token_index]

    def eat(self, token_type):
        if self.current_token.type == token_type:
            try:
                self.token_index += 1
                self.current_token = self.tokens[self.token_index]
                self.add_python_code(self.tokens[self.token_index-1], self.token_index-1)
                Expression.append_result(f"ate {self.current_token}")
            except IndexError as e:
                pass
            except Exception as e:
                print(f"Error {self.current_token}")
        else:
            self.error()

    def run_glc(self):
        pass

    def end_point(self):
        token = self.current_token
        if token.type == te.ENDPOINT:
            self.eat(te.ENDPOINT)
        # else:
        #     self.error()

    def run_thread(self, thread: ThreadWithReturnValue):
        thread.start()
        result = thread.join()
        Expression.append_result(result[2])
        return result

    @staticmethod
    def print_logs():
        print(f"Expression logs:\n")
        for i, log in enumerate(Expression.logs):
            print(f"{i}:{log}")

    @staticmethod
    def append_result(msg):
        Expression.logs.append(msg)

    def append_to_output(self, output):
        with open("output.py", "a") as file:
            file.write(output)

    def prepare_output(self):
        file = open("output.py", "w")
        file.close()

    @staticmethod
    def set_indent(num=1):
        Expression.indentation_level = num

    @staticmethod
    def increase_indent(*num):
        Expression.indentation_level += 1

    @staticmethod
    def decrease_indent(*num):
        Expression.indentation_level -= 1 if Expression.indentation_level > 0 else 0

    @staticmethod
    def indent(char='\\'):
        return Expression.indentation_level * char

    def add_python_code(self, token: Token, index: int):
        # print(f"{token}")
        # print(f"{Expression.indentation_level}: {token}")

        if index in Expression.output_indexes:
            return None

        Expression.output_indexes.append(index)
        output = ""

        if token.type in self.tokens_list.user_defined:
            output += Expression.indent()
            output += str(token.value)

        elif token.type in self.tokens_list.types:
            output += Expression.indent()
            output += ""
        elif token.type in [te.ENDPOINT, te.RBRACK]:
            output += "\n"

        elif token.type in [te.LBRACK]:
            output += ":\n"
        elif token.type in self.tokens_list.operators:
            output += " " + token.type.value + " "
        else:
            output += token.type.value

            if token.type not in [te.LPAREN, te.RPAREN, te.SHARINGAN, te.TAIJUTSU]:
                output += " "

        self.append_to_output(output)
