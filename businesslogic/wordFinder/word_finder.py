import re

from businesslogic.collection_helper import CollectionHelper


class WordFinder:
    def get(self, text):
        regex = re.compile('[ ():;,."«»-]')
        words = regex.split(text.lower())

        return CollectionHelper.calculate_counter(words).most_common()