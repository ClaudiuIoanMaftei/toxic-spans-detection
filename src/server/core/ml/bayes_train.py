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
        preproc.lower()
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
        lemmas = results.data["lemmas"]

        toxic_words = spans_to_words(entry[0], entry[1])

        punctuation = ".!?"

        for idx in range(0, len(tokens)):
            
            lemmas_in_sentence = []
            in_sen_idx = idx - 1
            while in_sen_idx>0 and not tokens[in_sen_idx] in punctuation:
                lemmas_in_sentence.append(lemmas[in_sen_idx])
                in_sen_idx -= 1

            in_sen_idx = idx + 1
            while in_sen_idx<len(tokens) and not tokens[in_sen_idx] in punctuation:
                lemmas_in_sentence.append(lemmas[in_sen_idx])
                in_sen_idx += 1       

            if tokens[idx] in toxic_words:
                bb.train(lemmas[idx], lemmas_in_sentence, "toxic")
            else:
                bb.train(lemmas[idx], lemmas_in_sentence, "non_toxic")

    bb.serialize()


###############
# Entry point #
###############

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            train_all_words()
        elif sys.argv[1] == "2":
            train_sentence()
