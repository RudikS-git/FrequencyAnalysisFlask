class Result:
    def __init__(self, one_letters, two_letters, three_letters, words, numbers_amount, text):
        self.one_letters = one_letters
        self.two_letters = two_letters
        self.three_letters = three_letters
        self.words = words
        self.numbers_amount = numbers_amount
        self.text = text

    def serialize(self):
        return {
            'one_letters': [e.serialize() for e in self.one_letters],
            'two_letters': [e.serialize() for e in self.two_letters],
            'three_letters': [e.serialize() for e in self.three_letters],
            'words': [e.serialize() for e in self.words],
            'amount_numbers': self.numbers_amount,
            'text': self.text,
            'amount_symbols': len(self.text)
        }