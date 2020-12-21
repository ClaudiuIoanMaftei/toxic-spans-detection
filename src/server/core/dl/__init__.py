import sys
from src.server.core import AnalyzerStrategy
from src.server.core.dl.cnn.executors.default_execution import DefaultExecution
from src.server.core.dl.parsing.vocabulary import Vocabulary

class DeepLearning(AnalyzerStrategy):
    _execution_strategy = None
    dataset_vocabulary = None

    def __init__(self):
        self._execution_strategy = DefaultExecution()
<<<<<<< HEAD
        self.dataset_vocabulary = []
        self.labels = []
        self.word_size = 0
        self.sentence_size = 0
=======
        self.dataset_vocabulary, labels, word_size, sentence_size = Vocabulary.from_csv(
            "datasets/tsd_train.csv")
        self._train({
            "word_size": word_size,
            "sent_size": sentence_size,
            "input": self.dataset_vocabulary,
            "labels": labels
        })
>>>>>>> d9a87289e0d210f8b401d8554297be8e417c2bd5

    def analyze(self, preprocessed) -> [int]:
        return None

    def _import_vocabulary(self, train_file = "datasets/tsd_train.csv" ):
        """
        Imports Vocabulary from external file
        :param train_file: required training data in csv file
        """
        self.dataset_vocabulary, self.labels, self.word_size, self.sentence_size = Vocabulary.from_csv(train_file)

    def _train(self, kwargs):
        """
        Trains the CNN with the given input data
        :return: None
        """
        self.strategy = DefaultExecution()
        self.strategy.init(**kwargs)

    def execute_training(self):
        self._import_vocabulary()
        self._train({
            "word_size": self.word_size,
            "sent_size": self.sentence_size,
            "input": self.dataset_vocabulary,
            "labels": self.labels
        })


if __name__ == "__main__":
    print("Deep Learning")
    dl = DeepLearning()
    if sys.argv[1] == "train":
        dl.execute_training()
