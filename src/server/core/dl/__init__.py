from src.server.core import AnalyzerStrategy
from src.server.core.dl.cnn.executors.default_execution import DefaultExecution
from src.server.core.dl.parsing.vocabulary import Vocabulary

class DeepLearning(AnalyzerStrategy):
    _execution_strategy = None
    dataset_vocabulary = None

    def __init__(self):
        self._execution_strategy = DefaultExecution()
        self.dataset_vocabulary, labels, word_size, sentence_size = Vocabulary.from_csv(
            "datasets/tsd_train.csv")
        self._train({
            "word_size": word_size,
            "sent_size": sentence_size,
            "input": self.dataset_vocabulary,
            "labels": labels
        })

    def analyze(self, preprocessed) -> [int]:
        return None

    def _train(self, kwargs):
        """
        Trains the CNN with the given input files
        :param input_directory: directory with one or more CSV files used as input data
        :return: None
        """
        self.strategy = DefaultExecution()
        self.strategy.init(**kwargs)


if __name__ == "__main__":
    print("Deep Learning")
    dl = DeepLearning()
