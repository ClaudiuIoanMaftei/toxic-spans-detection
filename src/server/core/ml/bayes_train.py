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

    debug_file = "train_debug.txt"
    debugf = open(debug_file, 'w', encoding="utf-8")

    bb = BayesBank()
    train_data = parse_data("tsd_train.csv")

    for entry in train_data:

        print(entry)

        debugf.write(str(entry[1]) + "\n")
        debugf.write(str(entry[0]) + "\n")

        toxic = ""
        for i in entry[0]:
            toxic += entry[1][i]
        debugf.write("\n" + str(toxic) + "\n")


        debugf.write("\n" + str(entry) + "\n")

        preproc = PreProcessor(entry[1])
        preproc.tokenize_sentences()
        preproc.lower()
        results = preproc.generate_results()

        sentences = results.data["sentences"]
        debugf.write(str(sentences) + "\n")

        for sentence in sentences:

            lemmas = []

            for token in sentence:
                lemmas.append(token["lemma"])

            for token in sentence:

                start_idx = token["idx"]
                stop_idx  = start_idx + len(token["token"]) - 1

                features = lemmas.copy()
                features.remove(token["lemma"])

                if start_idx in entry[0] and stop_idx in (entry[0]):
                    bb.train(token["lemma"], features, "toxic")
                    debugf.write(token["token"] + " " + str(start_idx) + ":" + str(stop_idx) + " toxic\n" + str(features) + "\n\n")
                else:
                    bb.train(token["lemma"], features, "nontoxic")
                    debugf.write(token["token"] + " " + str(start_idx) + ":" + str(stop_idx) + " nontoxic\n" + str(features) + "\n\n")

    bb.serialize()
    debugf.close()

###############
# Entry point #
###############

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            train_all_words()
        elif sys.argv[1] == "2":
            train_sentence()
