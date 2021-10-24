class SwimParts:
    @staticmethod
    def get(input_string, length):
        strings = []
        for i in range(len(input_string)):
            strings.append(input_string[i:i + length].lower())

        return strings
