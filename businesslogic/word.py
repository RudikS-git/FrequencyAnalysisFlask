from entity import Entity


class Word(Entity):
    def __init__(self, content, amount, frequency):
        self.content = content
        self.amount = amount
        self.frequency = frequency
