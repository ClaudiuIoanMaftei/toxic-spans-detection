from src.server.core import AnalyzerStrategy
from src.server.core.ml.bayes import BayesBank
from src.server.core.ml.features import FeatureSelector

class MachineLearning(AnalyzerStrategy):

    def __init__(self, method=0):
        self.bayes = BayesBank()
        self.bayes.load()
        self.feature_selector = FeatureSelector(method)

    def analyze(self, preproc) -> [int]:

        output = []
        feature_dic = self.feature_selector.features(preproc)
        text = feature_dic["text"]

        for token in feature_dic:

            if token == 'text':
                continue

            lemma = feature_dic[token]["lemma"]
            feature_list = feature_dic[token]["features"]

            if self.bayes.classify(lemma, feature_list) == "toxic":
                start = text.find(token)
                end = start + len(token)
                for i in range(start, end):
                    if i not in output:
                        output.append(i)


        output.sort()
        return output


if __name__ == "__main__":
    print("Machine Learning")
