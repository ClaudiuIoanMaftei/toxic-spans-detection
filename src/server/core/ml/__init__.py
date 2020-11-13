import nltk
from nltk.corpus import sentiwordnet as swn
from src.server.core import SingletonException, AnalyzerStrategy
from src.server.core.ml import tokenizer


class SentiWordNet:
    __instance = None

    @staticmethod
    def get_instance():
        if SentiWordNet.__instance is None:
            SentiWordNet()
        return SentiWordNet.__instance

    def __init__(self):
        if SentiWordNet.__instance is not None:
            raise SingletonException
        else:
            try:
                nltk.data.find('corpora/wordnet.zip/wordnet/')
                nltk.data.find('corpora/sentiwordnet.zip/sentiwordnet/')
            except:
                nltk.download('wordnet')
                nltk.download('sentiwordnet')
                print(nltk.data.find('corpora/wordnet.zip/wordnet/'))
                print(nltk.data.find('corpora/sentiwordnet.zip/sentiwordnet/'))
            SentiWordNet.__instance = self

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


class MachineLearning(AnalyzerStrategy):
    def __init__(self):
        pass

    def analyze(self, preprocessed) -> [int]:

        output = []
        tokens = tokenizer.tokenize(preprocessed)
        senti = SentiWordNet.get_instance()

        for token in tokens:
            if senti.query(token) > 0.1:
                start = preprocessed.find(token)
                end = start + len(token)
                for i in range(start, end):
                    output.append(i)
        return output


if __name__ == "__main__":
    print("Machine Learning")
