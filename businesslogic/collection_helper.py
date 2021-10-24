import collections


class CollectionHelper:
    @staticmethod
    def calculate_counter(input_list):
        counter = collections.Counter()

        for item in input_list:
            counter[item] += 1

        return counter
