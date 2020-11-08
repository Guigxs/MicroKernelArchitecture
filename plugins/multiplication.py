import CalculatorPlugin

class Multiplication(CalculatorPlugin.Plugin):
    def __init__(self):
        super().__init__()
        self.name = "Multiplication"
        self.operator = "*"


    def compute(self, a, b):
        return int(a) * int(b)