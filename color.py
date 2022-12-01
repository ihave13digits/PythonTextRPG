class Color:

    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def reset(self, c):
        self.r, self.g, self.b = c.r, c.g, c.b
