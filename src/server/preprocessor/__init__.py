import nltk


class PreprocResults:
    def __init__(self, normalized):
        self.normalized = normalized
        self.data = {}
        pass


class PreProcessor:
    __instance = None
    __corpus = None
    __tokens = None

    def __init__(self, corpus=""):
        PreProcessor.__instance = self
        PreProcessor.__corpus = self

    @staticmethod
    def get_instance():
        return PreProcessor.__instance

    def tokenize(self):
        pass

    def lemmatize(self):
        pass

    def generate_synonym_dictionary(self):
        pass

    def generate_punctuation_score(self):
        pass

    def generate_case_score(self):
        pass

    def generate_results(self):
        pass


if __name__ == "__main__":
    print("Preprocessing")
