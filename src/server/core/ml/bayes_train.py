import sys

from src.server.core.ml.bayes import BayesBank
from src.server.preprocessor  import PreProcessor
from src.server.core.ml.utils import parse_data, spans_to_words
from src.server.core.ml.features import  FeatureSelector

#######################
# Training Strategies #
#######################


# Takes the rests of the words in the message as features
def train(feature_strategy):
    bb = BayesBank()

    train_data = parse_data("tsd_train.csv")
    feature_selector = FeatureSelector(feature_strategy)

    for entry in train_data:

        print(entry)
        preproc = PreProcessor(entry[1])

        feature_dic = feature_selector.features(preproc)
        toxic_words = spans_to_words(entry[0], entry[1])

        for token in feature_dic:

            if token == 'text':
                continue

            lemma = feature_dic[token]["lemma"]
            features = feature_dic[token]["features"]

            if token in toxic_words:
                bb.train(lemma, features, "toxic")
            else:
                bb.train(lemma, features, "non_toxic")

    bb.serialize()


###############
# Entry point #
###############

if __name__ == "__main__":

    feature_method = 0
    if len(sys.argv) > 1 and int(sys.argv[1]) >= 0 and int(sys.argv[1]) <= 1:
        feature_method = int(sys.argv[1])

    train(int(sys.argv[1]))

