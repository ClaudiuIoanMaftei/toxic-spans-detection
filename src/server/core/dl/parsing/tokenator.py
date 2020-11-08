from src.server.core.dl.parsing.vocabulary import Vocabulary
import string


class Tokenator:

    def __init__(self):
        pass

    @staticmethod
    def tokenate(in_string):
        """
        Constructs a new vocabulary consisting of the words from the input string. Each word will be
        labelled and transformed into equal size vectors, that the other layers from the CNN can use
        :param in_string: input text
        """
        retval = {}
        word_dict = {}
        index = 1

        for token in in_string.split():
            word = token.strip(string.punctuation)

            if word in word_dict:
                retval[word_dict[word]] = token
            else:
                word_dict[word] = index
                retval[index] = word
                index += 1

        return Vocabulary(retval)
