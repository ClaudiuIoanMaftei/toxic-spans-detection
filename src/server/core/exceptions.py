class DetectionFailedException(Exception):
    """Exception raised by the core modules for failing the detection logic.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Detection failure"):
        self.message = message
        super().__init__(self.message)


class UninitializedException(Exception):
    """Exception raised by the core modules for incomplete/incorrect initialization.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Class has not been initialized"):
        self.message = message
        super().__init__(self.message)


class SingletonException(Exception):
    """Exception raised by the core modules for being singletone and already initialized.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Class is a singleton and already initialized"):
        self.message = message
        super().__init__(self.message)
