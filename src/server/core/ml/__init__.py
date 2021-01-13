from src.server.core import SingletonException, AnalyzerStrategy
from src.server.preprocessor import PreProcessor
from src.server.core.ml.bayes import BayesBank

class MachineLearning(AnalyzerStrategy):

    def __init__(self, method=0):
        self.bayes = BayesBank()
        self.bayes.load()
        self.__method = method

    def __all_words(self, preproc):

        output = []
        preproc.lower()
        preproc.tokenize()
        preproc.lemmatize()
        results = preproc.generate_results()

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]

        used_tokens = []

        uniq_lemmas = list(set(lemmas))

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            if token in used_tokens:
                continue

            lemmas_wo = uniq_lemmas.copy()
            lemmas_wo.remove(lemma)

            if self.bayes.classify(lemma, lemmas_wo) == "toxic":
                start = results.text.find(token)
                end = start + len(token)
                for i in range(start, end):
                    if i not in output:
                        output.append(i)

            used_tokens.append(token)

        output.sort()
        return output

    def __sentence(self, preproc):

        output = []

        preproc.tokenize_sentences()
        preproc.lower()
        results = preproc.generate_results()

        sentences = results.data["sentences"]

        for sentence in sentences:

            lemmas = []

            for token in sentence:
                lemmas.append(token["lemma"])

            for token in sentence:

                start_idx = token["idx"]
                stop_idx  = start_idx + len(token["token"]) - 1

                features = lemmas.copy()
                features.remove(token["lemma"])

                if self.bayes.classify(token["lemma"], features) == "toxic":
                    for i in range(start_idx, stop_idx+1):
                        if i not in output:
                            output.append(i)

        output.sort()
        return output


    def analyze(self, preproc) -> [int]:

        if self.__method == 0:
            return self.__all_words(preproc)
        elif self.__method == 1:
            return self.__sentence(preproc)


if __name__ == "__main__":
    print("Machine Learning")
