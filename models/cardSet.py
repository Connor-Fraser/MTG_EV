class Set:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return self.code + ': ' + self.name