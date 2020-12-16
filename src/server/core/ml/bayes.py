import math, sys, csv, json

from src.server.preprocessor import PreProcessor

# Global vars
data_path = "src/server/core/ml/data/"
#####################################

class Bayes:

    def __init__(self, data=None):
        self.alpha = 1
        self.categories = {}
        self.features_count = {}
        self.total_features = 0

        if data != None:
            self.alpha = data["alpha"]
            self.categories = data["categories"]
            self.features_count = data["features_count"]
            self.total_features = data["total_features"]

    def train(self, features, category):

        if not category in self.categories:
            self.categories[category] = {
                "count": 1,
                "features": {}
            }
        else:
            self.categories[category]["count"] += 1

        for feature in features:

            self.total_features += 1

            if not feature in self.features_count:
                self.features_count[feature] = 1
            else:
                self.features_count[feature] += 1

            if not feature in self.categories[category]["features"]:
                self.categories[category]["features"][feature] = 1
            else:
                self.categories[category]["features"][feature] += 1


    def classify(self, features):

        log_probabilities = {}
        entries_count = 0


        for category in self.categories:
            entries_count += self.categories[category]["count"]

        for category in self.categories:

            category_probability = self.categories[category]["count"] / entries_count
            log_probabilities[category] = math.log(category_probability)

            total_features = 0
            for feature in self.categories[category]["features"]:
                total_features += self.categories[category]["features"][feature]

            for feature in features:
                count_in_category = self.alpha

                if feature in self.categories[category]["features"]:
                    count_in_category += self.categories[category]["features"][feature]

                likelihood = count_in_category / ( total_features + len(self.features_count.keys()) )
                log_probabilities[category] += math.log(likelihood)

        max_probability = float("-inf")
        final_category = None
        for category in log_probabilities:
            if log_probabilities[category] >= max_probability:
                max_probability = log_probabilities[category]
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
            return None

        return self.classifiers[word].classify(features)

    def serialize(self):
        data_bank = {
            "classifiers": {}
        }

        for word in self.classifiers:
            data_bank["classifiers"][word] = {
                "alpha": self.classifiers[word].alpha,
                "categories" : self.classifiers[word].categories,
                "features_count" : self.classifiers[word].features_count,
                "total_features": self.classifiers[word].total_features
            }

        file = open(data_path + "model.dat", 'w')
        file.write(json.dumps(data_bank, indent=4))
        #file.write(json.dumps(data_bank))
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
