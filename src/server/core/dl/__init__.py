import sys
from src.server.core import AnalyzerStrategy
from src.server.core.dl.cnn.executors.default_execution import DefaultExecution
from src.server.core.dl.parsing.vocabulary import Vocabulary

class DeepLearning(AnalyzerStrategy):
    _execution_strategy = None
    dataset_vocabulary = None

    def __init__(self):
        self._execution_strategy = DefaultExecution()
        self.dataset_vocabulary = []
        self.labels = []
        self.word_size = 0
        self.sentence_size = 0
        self.model = 0

    def analyze(self, preprocessed) -> [int]:
        return None

    def _import_vocabulary(self, training_data_path):
        """
        Imports Vocabulary from external files
        :param train_file: required training data in csv files
        """
        self.dataset_vocabulary, self.labels, self.word_size, self.sentence_size = Vocabulary.from_csv(training_data_path)

    def _train(self, kwargs):
        """
        Trains the CNN with the given input data
        :return: None
        """
        self.strategy = DefaultExecution()
        self.model = self.strategy.init(**kwargs)
        if self.model != None:
            self.model.save("fashion_model_dropout.h5py")

    def execute_training(self, training_data_path = "datasets/tsd_train.csv"):
        self._import_vocabulary(training_data_path)
        self._train({
            "word_size": self.word_size,
            "sent_size": self.sentence_size,
            "input": self.dataset_vocabulary,
            "labels": self.labels
        })


if __name__ == "__main__":
    print("Deep Learning")
    dl = DeepLearning()
    if sys.argv[1] == "-train":
        try:
            dl.execute_training(sys.argv[2])
        except:
            dl.execute_training()
