from interfaces.Afd import Afd


class If(Afd):
    def __init__(self):
        super(If, self).__init__();

    def handle(self, input_data: str) -> bool:
        for chr in input_data:
