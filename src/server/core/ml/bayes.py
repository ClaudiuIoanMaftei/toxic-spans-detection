import math, sys, csv, json

from src.server.preprocessor import PreProcessor

# Global vars
data_path = "src/server/core/ml/data/"
#####################################

class Bayes:

    def __init__(self, data=None):
        self.alpha = 1
        self.categories = {}
        self.unique_features = []
        self.entries_count = 0

        if data != None:

            self.alpha = data["alpha"]
            self.categories = data["categories"]
            self.unique_features = data["unique_features"]
            self.entries_count = data["entries_count"]

    def train(self, features, category):

        self.entries_count += 1

        if not category in self.categories:
            self.categories[category] = {
                "count": 1,
                "features": {},
                "features_count" : 0
            }
        else:
            self.categories[category]["count"] += 1

        for feature in features:

            if not feature in self.unique_features:
                self.unique_features.append(feature)

            if not feature in self.categories[category]["features"]:
                self.categories[category]["features"][feature] = 1
            else:
                self.categories[category]["features"][feature] += 1


    def classify(self, features):

        if self.entries_count == 0:
            return

        max_probability = float("-inf")
        final_category = None

        for category in self.categories:

            apriori = self.categories[category]["count"] / self.entries_count
            probability = math.log(apriori)

            for feature in features:

                likelihood = self.alpha
                if feature in self.categories[category]["features"]:
                    likelihood += self.categories[category]["features"][feature]

                likelihood = likelihood / (self.categories[category]["features_count"] + self.alpha * len(self.unique_features))
                probability += math.log(likelihood)

            if(probability > max_probability):
                max_probability = probability
                final_category = category


        return final_category



class BayesBank:

    def __init__(self):
        self.classifiers = {}

    def train(self, word, features, category):

        if not word in self.classifiers:
            self.classifiers[word] = Bayes()

        self.classifiers[word].train(features, category)

    def classify(self, word, features):

        if not word in self.classifiers:
            return "non_toxic"

        return self.classifiers[word].classify(features)

    def serialize(self):
        data_bank = {
            "classifiers": {}
        }

        for word in self.classifiers:
            data_bank["classifiers"][word] = {
                "alpha": self.classifiers[word].alpha,
                "categories" : self.classifiers[word].categories,
                "unique_features" : self.classifiers[word].unique_features,
                "entries_count": self.classifiers[word].entries_count
            }

        file = open(data_path + "model.dat", 'w')
        #file.write(json.dumps(data_bank, indent=4))
        file.write(json.dumps(data_bank))
        file.close()


    def load(self):
        file = open(data_path+"model.dat", 'r', encoding="utf-8")
        data_bank = json.loads(file.read())["classifiers"]
        file.close()

        for word in data_bank:
            self.classifiers[word] = Bayes(data_bank[word])



def demo():

    bb = BayesBank()
    bb.train("idiot", ["You", "are", "an", "idiot"], "toxic")
    bb.train("idiot", ["Fine", "i", "guess", "you", "are", "my", "little", "idiot"], "nontoxic")

    #an idiot
    print(bb.classify("idiot", ["an"]))

    #my little idiot
    print(bb.classify("idiot", ["my", "little"]))

if __name__ == "__main__":
	demo()
