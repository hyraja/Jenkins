class Cal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return f'addition = {self.x + self.y }'

    def sub(self):
        return f'substraction = {self.x - self.y }'

    def mul(self):
        return f'multiplication = {self.x * self.y }'

    def div(self):
        return f'division = {self.x / self.y }'
