import re


class NumbersCounter:
    def get(self, text):
        regex = re.compile('\b*\D*[\d]+\D*\b*')
        return len(regex.findall(text))
