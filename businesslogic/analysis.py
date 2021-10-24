from businesslogic.entity import Entity

class Analysis:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        if(not text):
            raise ValueError("Text mustn't be null!")

        self.text = text

    def get_text(self):
        return self.text

    def get_words(self, words_finder):
        return words_finder.get(self.text)

    def get_letter(self, letter_finder):
        return letter_finder.get(self.text, 1)

    def get_two_letter(self, letter_finder):
        return letter_finder.get(self.text, 2)

    def get_three_letter(self, letter_finder):
        return letter_finder.get(self.text, 3)

    def get_numbers(self, numbers_counter):
        return numbers_counter.get(self.text)

    def get_frequence(self, frequence_calculation, input_list, total_amount):
        new_list = []
        for item in input_list:
            frequency = frequence_calculation.get(item[1], total_amount)
            entity = Entity(item[0], item[1], frequency)
            new_list.append(entity)

        return new_list
