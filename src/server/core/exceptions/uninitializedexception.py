class UninitializedException(Exception):
    """Exception raised by the core modules for incomplete/incorrect initialization.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Class has not been initialized"):
        self.message = message
        super().__init__(self.message)

