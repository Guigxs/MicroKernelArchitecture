import CalculatorPlugin

class Substract(CalculatorPlugin.Plugin):
    def __init__(self):
        super().__init__()
        self.name = "Substraction"
        self.operator = "-"


    def compute(self, a, b):
        return int(a) - int(b)