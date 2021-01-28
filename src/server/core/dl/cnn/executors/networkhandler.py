from ....exceptions import DetectionFailedException


class NetworkHandler:
    """
    Abstract class for creating, training and adjusting a Keras CNN
    """

    def __init__(self):
        self._model = None

    def init(self, **kwargs):
        """
        initialize the execution chain
        :param kwargs: arguments used for training/tuning the layers
        :return: None
        """
        raise BaseException("Execution strategy must implement init method")

    def predict(self, input_text):
        try:
            cnn_input = self.transform(input_text)
            self._model.predict(cnn_input)
        except Exception as e:
            raise DetectionFailedException(e)

    def transform(self, input_text):
        """
        Function called by the predict method before running the CNN workflow.
        This is used to normalize the input and should be implemented by the concrete handler class
        :param input_text:
        :return:
        """
        raise Exception("Transform method should be implemented.")