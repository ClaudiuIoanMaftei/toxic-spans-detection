class FeatureSelector:

    def __init__(self, method=0):
        self.method = method

        if self.method == 0:
            print("Feature selector __all_words")
        elif self.method == 1:
            print("Feature selector __bigrams")

    def __all_words(self, preproc):

        features_dic = {}

        preproc.lower()
        preproc.tokenize()
        preproc.lemmatize()
        results = preproc.generate_results()

        features_dic["text" ] = results.text

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]
        uniq_lemmas = list(set(lemmas))

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            lemmas_wo = list(uniq_lemmas)
            lemmas_wo.remove(lemma)

            features_dic[token] = { "lemma" : lemma, "features" : lemmas_wo }

        return features_dic


    def __bigrams(self, preproc):

        features_dic = {}

        preproc.lower()
        preproc.tokenize()
        preproc.remove_stopwords()
        preproc.lemmatize()
        results = preproc.generate_results()

        features_dic["text" ] = results.text

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]
        uniq_lemmas = list(set(lemmas))

        bigrams = []
        for idx in range(0, len(lemmas)-1):
            bigram = lemmas[idx] + " " + lemmas[idx+1]
            if not bigram in bigrams:
                bigrams.append(bigram)

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            lemmas_wo = list(uniq_lemmas)
            lemmas_wo.remove(lemma)

            features = lemmas_wo + bigrams

            features_dic[token] = { "lemma" : lemma, "features" : features }

        return features_dic

    def features(self, preproc):
        if self.method == 0:
            return self.__all_words(preproc)
        elif self.method == 1:
            return self.__bigrams(preproc)

