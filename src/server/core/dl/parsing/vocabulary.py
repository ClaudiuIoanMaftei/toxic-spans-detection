import pandas as pd
import spacy

import numpy as np
import re
import multiprocessing
from time import time
from collections import defaultdict

from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec


class Vocabulary:
    TEST_RUN = True
    _w2v_model = None

    def __init__(self, tokens):
        """
        Constructs the row matrix from the labeled word tokens (for testing)
        """
        self._tokens = tokens

    @staticmethod
    def create(string):
        # Creates a new vocabulary using string splitting, used for debugging
        return Vocabulary(string.split())

    @staticmethod
    def from_csv(path):
        df = pd.read_csv(path)
        nlp = spacy.load('en', disable=['ner', 'parser'])
        start_time = time()

        # to lowercase and remove non alphabetic characters
        lowercase = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in df['text'])

        # lemmatization
        txt = [cleaning(doc) for doc in nlp.pipe(lowercase, batch_size=5000, n_threads=-1)]
        print('Time to clean up everything: {} mins'.format(round((time() - start_time) / 60, 2)))

        df_clean = pd.DataFrame({'clean': txt})
        df_clean = df_clean.dropna().drop_duplicates()

        sentences = [row.split() for row in df_clean['clean']]

        word_freq = defaultdict(int)
        for sent in sentences:
            for i in sent:
                word_freq[i] += 1
        len(word_freq)

        cores = multiprocessing.cpu_count()
        w2v_model = Word2Vec(min_count=20,
                             window=2,
                             size=100,
                             sample=6e-5,
                             alpha=0.03,
                             min_alpha=0.0007,
                             negative=20,
                             workers=cores - 1)

        t = time()

        w2v_model.build_vocab(sentences, progress_per=10000)

        print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

        t = time()

        w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)

        print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))

        w2v_model.init_sims(replace=True)
        print("W2V model initialized successfully.")

        max_shape = max([len(x) for x in sentences])

        cnn_input = []
        for i, sent in sentences:
            sentence_matrix = np.zeros([max_shape, 100])  # [number of words, 100 characters/word]
            for i, word in enumerate(sent):
                try:
                    sentence_matrix[i] = w2v_model.wv.get_vector(word)
                except KeyError as e:
                    pass
            cnn_input.append(sentence_matrix)

        print(len(cnn_input))

        return np.array(cnn_input)

    def get_tokens(self):
        return self._tokens


def cleaning(doc):
    """
    See https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial
    :param doc:
    :return:
    """
    # Lemmatizes and removes stopwords
    # doc needs to be a spacy Doc object
    txt = [token.lemma_ for token in doc if not token.is_stop]
    # Word2Vec uses context words to learn the vector representation of a target word,
    # if a sentence is only one or two words long,
    # the benefit for the training is very small
    if len(txt) > 2:
        return ' '.join(txt)
