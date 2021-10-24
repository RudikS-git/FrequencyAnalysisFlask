from entity import Entity


class Letter(Entity):
    def __init__(self, content, amount, frequency):
        self.content = content
        self.amount = amount
        self.frequency = frequency
