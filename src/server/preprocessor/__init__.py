import nltk

#kept this way as to use a Builder DP
class PreprocResults:
    def __init__(self):
        self.data = {}


class PreProcessor:
    __instance = None
    __lemmatizer = nltk.stem.WordNetLemmatizer()

    __corpus = None
    __tokens = None
    __lemmas = None
    __synonyms= None
    __punctuation_score = None
    __case_score= None

    def __init__(self, corpus=""):
        PreProcessor.__instance = self
        PreProcessor.__corpus = corpus
        PreProcessor.__tokens = None

    @staticmethod
    def get_instance():
        return PreProcessor.__instance

    def lower(self):
        """
        Lower all letters in the corpus
        :return:
        """
        self.__corpus=self.__corpus.lower()

    def tokenize(self):
        """
        Create the token list
        :return:
        """
        self.__tokens=nltk.word_tokenize(self.__corpus)

    def lemmatize(self):
        """
        Create the lemma list from the token list (created if not existing)
        :return:
        """
        if self.__lemmas is None:
            self.tokenize()

        pos_list=nltk.pos_tag(self.__tokens)

        self.__lemmas=[]
        for token,pos in pos_list:
            if pos[0]=='J':
                pos=nltk.corpus.wordnet.ADJ
            elif pos[0]=="V":
                pos=nltk.corpus.wordnet.VERB
            elif pos[0]=="N":
                pos=nltk.corpus.wordnet.NOUN
            elif pos[0]=="R":
                pos=nltk.corpus.wordnet.ADC
            else:
                pos=nltk.corpus.wordnet.NOUN

            lemma = self.__lemmatizer.lemmatize(token, pos)
            if nltk.corpus.wordnet.morphy(lemma) is not None:
                self.__lemmas.append(nltk.corpus.wordnet.morphy(lemma))
            else:
                self.__lemmas.append(lemma)

    def remove_stopwords(self):
        """
        Remove stop words from the token list (if it exists)
        Remove stop words from the lemma list (if it exists)
        :return:
        """
        if self.__tokens is not None:
            self.__tokens=[token for token in self.__tokens if not token in nltk.corpus.stopwords.words('english')]

        if self.__lemmas is not None:
            self.__lemmas = [lemma for lemma in self.__lemmas if not lemma in nltk.corpus.stopwords.words('english')]

    def remove_punctuation(self):
        """
        Remove punctuation from the token list (if it exists)
        Remove punctuation from the lemma list (if it exists)
        :return:
        """
        if self.__tokens is not None:
            self.__tokens=[token for token in self.__tokens if any(char.isalnum() for char in token)]

        if self.__lemmas is not None:
            self.__lemmas=[lemma for lemma in self.__lemmas if any(char.isalnum() for char in lemma)]

    def generate_synonym_dictionary(self):
        """
        Generates a dictionary containing lemma: [array of synonyms] (generates the lemma list if not existing)
        :return:
        """
        if self.__lemmas is None:
            self.lemmatize()

        self.__synonyms={}

        for lemma in self.__lemmas:
            synset = nltk.corpus.wordnet.synsets(lemma)
            for syn in synset:
                for syn_lemma in syn.lemmas():
                    if not lemma in self.__synonyms:
                        self.__synonyms[lemma]=[]

                    self.__synonyms[lemma].append(syn_lemma.name())

        for key in self.__synonyms:
            self.__synonyms[key]=list(set(self.__synonyms[key]))

    def generate_punctuation_score(self):
        """
        Generates the ratio of punctuation/characters
        :return:
        """
        punctuation=len([char for char in self.__corpus if not char.isalnum() and char not in " \n\t"])
        self.__punctuation_score = punctuation / len(self.__corpus)


    def generate_case_score(self,weight=0.5):
        """
        Generates a score based on the upper/lowercase amount and its frequent change (as it marks sarcasm)
        :param weight: the lerp weight of the upper/lowercase amount to frequent change; may include values outside of [0,1]
        :return:
        """

        upper=0
        lower=0
        changes=0
        prevcase=None

        for char in self.__corpus:
            if char.lower()!=char.upper():
                if char.islower():
                    lower+=1
                    newcase="l"
                else:
                    upper+=1
                    newcase="u"

                if prevcase!=None and newcase!=prevcase:
                    changes+=1
                prevcase=newcase

            else:
                prevcase=None

        upper_lower=upper/(upper+lower)
        freq_change=changes/(upper+lower)

        self.__case_score= upper_lower + weight * (freq_change - upper_lower) #lerp

    def generate_results(self):
        """
        Generates the results of the preprocessing
        :return PreprocResults:
        """
        results=PreprocResults()
        results.text = self.__corpus
        if self.__tokens is not None:
            results.data["tokens"]=self.__tokens
        if self.__lemmas is not None:
            results.data["lemmas"] = self.__lemmas
        if self.__synonyms is not None:
            results.data["synonyms"] = self.__synonyms
        if self.__punctuation_score is not None:
            results.data["punctuation_score"] = self.__punctuation_score
        if self.__case_score is not None:
            results.data["punctuation_score"] = self.__case_score

        return results

    def preprocess(self, text):
        self.__corpus = text
        self.__tokens = None
        self.__lemmas = None

        self.tokenize()
        self.lemmatize()
        self.generate_synonym_dictionary()

        return self.generate_results()



if __name__ == "__main__":
    p=PreProcessor()
    print(p.preprocess("THese are some test examples! Hello! Oh, how wOnDeRoUs the technological makings of man...").data)


