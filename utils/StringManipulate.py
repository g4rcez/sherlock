from re import sub


class StringManipulate():
    @staticmethod
    def inverseReplace(text, word, replaced):
        parts = text.split(word)
        return word.join(replaced * len(x) for x in parts)

    @staticmethod
    def removeNonNumbers(string):
        return sub("[^0-9]", "", string)

    # simbols expected an array
    @staticmethod
    def removeSpecifieds(string, simbols):
        for simbol in simbols:
            string = string.replace(simbol, '')
        return string
