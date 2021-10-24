from businesslogic.collection_helper import CollectionHelper
from businesslogic.letter_finder_way.swim_parts import SwimParts


class LetterFinder:
    def get(self, text, length):
        parts = SwimParts.get(text, length)
        filter_list = filter(lambda x: (len(x) == length and x.isalpha()), parts)

        return CollectionHelper.calculate_counter(filter_list).most_common()

