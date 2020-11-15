from src.server.core.interfaces import Handler


class FeedForwardNetworkLayer(Handler):
    """
    The FNN is essentially a `:class:ConvolutionalLayer` that has only a 1x1 kernel size. This is used for fine tuning
    the weights and should be one of the last stages of the execution chain.
    """
    def __init__(self):
        pass

    def execute(self, args) -> None:
        pass

    def train(self, **kwargs):
        """
        Begin training the layer
        :param kwargs: arguments for training must include the input files path (.csv), bias and weights matrix
        :return: None
        :return: None
        """
        pass
