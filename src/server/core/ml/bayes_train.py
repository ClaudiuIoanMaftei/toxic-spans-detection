import sys

from src.server.core.ml.bayes import BayesBank
from src.server.preprocessor  import PreProcessor
from src.server.core.ml.utils import parse_data, spans_to_words

#######################
# Training Strategies #
#######################

# Takes the rests of the words in the message as features

def train_all_words():
    bb = BayesBank()

    print("train_all_words")

    train_data = parse_data("tsd_train.csv")


    for entry in train_data:
        print(entry)
        
        preproc = PreProcessor(entry[1])
        preproc.tokenize()
        preproc.lemmatize()

        results = preproc.generate_results()

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]
        uniq_lemmas = list(set(lemmas))

        toxic_words = spans_to_words(entry[0], entry[1])

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            lemmas_wo = list(uniq_lemmas)
            lemmas_wo.remove(lemma)
            for i in range(0, len(lemmas_wo)):
                lemmas_wo[i] = lemmas[i]

            if token in toxic_words:
                bb.train(lemma, lemmas_wo, "toxic")
            else:
                bb.train(lemma, lemmas_wo, "non_toxic")

    bb.serialize()

# Takes only the words that are in the same sentence
def train_sentence():
    bb = BayesBank()
    train_data = parse_data("tsd_train.csv")

    for entry in train_data:
        print(entry)
        preproc = PreProcessor(entry[1]) 
        preproc.tokenize()
        preproc.lemmatize()

        results = preproc.generate_results()

        tokens = results.data["tokens"]
        lemmas = results.data["lammas"]

        toxic_words = spans_to_words(entry[0], entry[1]) 

               



###############
# Entry point #
###############

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            train_all_words()
