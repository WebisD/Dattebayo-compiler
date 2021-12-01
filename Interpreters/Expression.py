from Interpreters.RThread import ThreadWithReturnValue
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

    def __init__(self, token_index: int, token_array=None):
        #self.__dict__ = self.__shared_state
        if token_array is None:
            token_array = []
        self.tokens = token_array
        self.current_token: Token = token_array[token_index]
        self.token_index = token_index
        self.marker_index = 0

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
        else:
             self.error()

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
