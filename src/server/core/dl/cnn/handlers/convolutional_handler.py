from src.server.core.interfaces import Handler


class ConvolutionalLayer(Handler):
    """
    The convolutional neural network is the main layer of the DL component. This will contain the kernel matrices
    that will be executed. This layer must also be trained before usage.
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
        """
        pass
