class Plugin(object):
    def __init__(self):
        self.name = "UNKONWN"
        self.operator = "UNKONWN"

    def compute(self, a, b):
        raise NotImplementedError