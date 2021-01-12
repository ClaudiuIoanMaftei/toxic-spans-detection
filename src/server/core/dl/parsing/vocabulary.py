class Vocabulary:

    def __init__(self, tokens):
        """
        Constructs the row matrix from the labeled word tokens (for testing)
        """
        self._tokens = tokens

    @staticmethod
    def create(string):
        # Creates a new vocabulary using string splitting, used for debugging
        return Vocabulary(string.split())

    def get_tokens(self):
        return self._tokens
