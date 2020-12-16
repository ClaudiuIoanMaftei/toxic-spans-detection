import nltk
from nltk.corpus import sentiwordnet as swn
from src.server.core import SingletonException, AnalyzerStrategy
from src.server.preprocessor import PreProcessor
from src.server.core.ml.bayes import BayesBank


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

    def senti_query(self, word):
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
        self.bayes = BayesBank()
        self.bayes.load()

    def analyze(self, preproc) -> [int]:

        output = []
        preproc.lower()
        preproc.tokenize()
        preproc.lemmatize()
        results = preproc.generate_results()

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]

        uniq_lemmas = list(set(lemmas))

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            lemmas_wo = list(uniq_lemmas)
            lemmas_wo.remove(lemma)

            if self.bayes.classify(lemma, lemmas_wo) == "toxic":
                start = results.text.find(token)
                end = start + len(token)
                for i in range(start, end):
                    output.append(i)

        return output

if __name__ == "__main__":
    print("Machine Learning")
