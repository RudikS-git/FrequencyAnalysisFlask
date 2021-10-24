class Entity:
    def __init__(self, content, amount, frequency):
        self.content = content
        self.amount = amount
        self.frequency = frequency

    def serialize(self):
        return {
            'content': self.content,
            'amount': self.amount,
            'frequency': self.frequency,
        }
