from src.server.core.dl.parsing.vocabulary import Vocabulary


class Tokenator:
    def __init__(self):
        pass

    def tokenate(self, string):
        """
        Constructs a new vocabulary consisting of the words from the input string. Each word will be
        labelled and transformed into equal size vectors, that the other layers from the CNN can use
        :param string: input text
        """
        return Vocabulary([string])
