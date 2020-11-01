class DetectionFailedException(Exception):
    """Exception raised by the core modules for failing the detection logic.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Detection failure"):
        self.message = message
        super().__init__(self.message)

