from .. import exceptions as core_exceptions
from .. import interfaces as core_interfaces
from . import tokenizer

import sys
import nltk
from nltk.corpus import sentiwordnet as swn


class SentiWordNet:

    def query(self, word):
        results = list(swn.senti_synsets(word))
        pos = 0
        neg = 0
        count = 0

        for result in results:
            if result.synset.name().split(".")[0] == word:
                pos += result.pos_score()
                neg += result.neg_score()
                count += 1

        if count > 0:
            return neg / count - pos / count
        else:
            return 0




class MachineLearning(core_interfaces.AnalyzerStrategy):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:

        output = []
        tokens = tokenizer.tokenize(preprocessed)
        senti = SentiWordNet()

        for token in tokens:
            if(senti.query(token) > 0.1):
                start = preprocessed.find(token)
                end = start + len(token)
                for i in range(start, end):
                    output.append(i)
        return output


if __name__ == "__main__":

    ml = MachineLearning()
    print("MachineLearning")

    if len(sys.argv) > 1:
        if sys.argv[1] == "setup":
            nltk.download('sentiwordnet')
    else:
        senti = SentiWordNet()
        print(senti.query("stupid"))




