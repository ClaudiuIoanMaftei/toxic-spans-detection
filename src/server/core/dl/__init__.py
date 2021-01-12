# import sys
from src.server.core import AnalyzerStrategy
from src.server.core.dl.cnn.executors.kerasnetworkhandler import KerasNetworkHandler
from src.server.core.dl.parsing.vocabulary import Vocabulary


class DeepLearning(AnalyzerStrategy):
    network_handler = None
    dataset_vocabulary = None
    validation_vocabulary = None

    def __init__(self):
#         self.network_handler = KerasNetworkHandler()
#         self.dataset_vocabulary = []
#         self.labels = []
#         self.word_size = 0
#         self.sentence_size = 0
#         self.model = 0
        self.network_handler = KerasNetworkHandler()
        self.dataset_vocabulary, labels, word_size, sentence_size = Vocabulary.from_csv(
            "datasets/tsd_train.csv")
        self.validation_vocabulary, validation_labels, validation_word_size, validation_sentence_size = \
            Vocabulary.from_csv("datasets/tsd_trial.csv")
        self._train({
            "word_size": word_size,
            "sent_size": sentence_size,
            "train_input": self.dataset_vocabulary,
            "train_labels": labels,
            "validation_input": self.validation_vocabulary,
            "validation_labels": validation_labels
        })

    def analyze(self, preprocessed) -> [int]:
        try:
            return self.network_handler.predict(preprocessed)
        except Exception: # Silent failure untill network is ready
            return None

#     def _import_vocabulary(self, training_data_path):
#         """
#         Imports Vocabulary from external files
#         :param train_file: required training data in csv files
#         """
#         self.dataset_vocabulary, self.labels, self.word_size, self.sentence_size = Vocabulary.from_csv(training_data_path)

    def _train(self, kwargs):
        """
        Trains the CNN with the given input files
        :param input_directory: directory with one or more CSV files used as input data
        :return: None
        """
#         self.strategy = DefaultExecution()
#         self.model = self.strategy.init(**kwargs)
#         if self.model is not None:
#             self.model.save("fashion_model_dropout.h5py")

#     def execute_training(self, training_data_path = "../../../../datasets/tsd_train.csv"):
#         self._import_vocabulary(training_data_path)
#         self._train({
#             "word_size": self.word_size,
#             "sent_size": self.sentence_size,
#             "input": self.dataset_vocabulary,
#             "labels": self.labels
#         })
        self.strategy = KerasNetworkHandler()
        self.strategy.init(**kwargs)


if __name__ == "__main__":
    print("Deep Learning")
    dl = DeepLearning()
#     if sys.argv[1] == "-train":
#         try:
#             dl.execute_training(sys.argv[2])
#         except:
#             dl.execute_training()
