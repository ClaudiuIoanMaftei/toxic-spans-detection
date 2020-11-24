from src.server.preprocessor import PreProcessor
import sys, re, csv, json, bayesian

# Global vars
data_path = "src/server/core/ml/data/"
#####################################


class Bayes:
    def __init__(self, bayes_type=0):
        self.bayes_type = bayes_type

    def parse_train_data(self):
        file = open(data_path + "tsd_train.csv", encoding="utf-8")
        entities = []
        csvreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in list(csvreader)[1:]:
            spans = []
            text = row[1]
            spans_text = row[0][1:-1]
            for number in spans_text.split(", "):
                if number is not '':
                    spans.append(int(number))

            entities.append([spans, text])
        return entities

    def train_full(self):
        print("Training full")
        train_data = self.parse_train_data()
        out_data = {}

        for entry in train_data:
            preproc = PreProcessor()
            results = preproc.preprocess(entry[1])

            tokens = results.data["tokens"]
            lemmas = results.data["lemmas"]
            uniq_lemmas = list(set(lemmas))
            toxic_words = []

            curr_word = ""
            last_idx = 0
            if len(entry[0]) > 0:
                last_idx = entry[0][0]

            for idx in entry[0]:

                curr_word += entry[1][idx]
                if idx > last_idx+1:
                    toxic_words += curr_word.split(" ")
                    curr_word = ""
                last_idx = idx
            if curr_word != "":
                toxic_words += curr_word.split(" ")

            for idx in range(0, len(tokens)):
                token = tokens[idx]
                lemma = lemmas[idx]

                lemmas_wo = list(uniq_lemmas)
                lemmas_wo.remove(lemma)

                if lemma not in out_data:
                    out_data[lemma] = {"toxic": [], "non_toxic": []}

                if token in toxic_words:
                    out_data[lemma]["toxic"].append(" ".join(lemmas_wo))
                else:
                    out_data[lemma]["non_toxic"].append(" ".join(lemmas_wo))


        file = open(data_path+"f.dat", 'w')
        file.write(json.dumps(out_data, indent=4))
        file.close()

    def train_sen(self):
        print("Training sentences")

    def train_pos(self):
        print("Training part of speech")

    def train(self):
        if self.bayes_type == 0:
            self.train_full()
        elif self.bayes_type == 1:
            self.train_sen()
        elif self.bayes_type == 2:
            self.train_pos()
        else:
            print("Inavlid bayes type: " + str(self.bayes_type))


    def load(self):
        if self.bayes_type == 0:
            file = open(data_path+"f.dat", 'r', encoding="utf-8")
            self.data = json.loads(file.read())
            file.close()
        else:
            pass

    def classify(self, lemma, context):
        if self.data is None:
            return None

        return bayesian.classify(context, {
            "toxic": self.data[lemma]["toxic"],
            "non_toxic": self.data[lemma]["non_toxic"]
        })

def train_classifier(bayes_type):
    bayes = Bayes(bayes_type)
    bayes.train()


def test_classifier(bayes_type):
    bayes = Bayes(0)
    bayes.load()
    print(bayes.classify("joke", "This man is a sickening, mentally ill joke."))


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == "train":
            if len(sys.argv) > 2:
                train_classifier(sys.argv[2])
            else:
                train_classifier(0)
        elif sys.argv[1] == "test":
            test_classifier("You are an idiot")