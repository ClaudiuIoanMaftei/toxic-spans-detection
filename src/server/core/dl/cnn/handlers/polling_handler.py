from src.server.core.interfaces import Handler


class PollingLayer(Handler):
    """
    A polling layer defines a strategy for reducing the processed input of a `:class:`ConvolutionalLayer`.
    Implementations for this can be using kNN, weighted subsampling, etc.
    """
    def __init__(self):
        pass

    def execute(self, args) -> None:
        pass

    def apply(self, cnn, **kwargs):
        """
        Applies the polling implementation over the given convolutional layer
        :param cnn:
        :param kwargs:
        :return:
        """
        pass
