from src.server.core import SingletonException, AnalyzerStrategy
from src.server.preprocessor import PreProcessor
from src.server.core.ml.bayes import BayesBank

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
