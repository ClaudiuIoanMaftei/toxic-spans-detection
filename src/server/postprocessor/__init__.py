from abc import abstractmethod


# Document : int []
# An array of indexes from analyzed text where Document[i] represents position of detected toxic span element.
# Example: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16] in text "You're ridiculous"


class PostProcessor:
    def __init__(self, documents = None):
        self.documents = documents

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


if __name__ == "__main__":
    print("Postprocessing")
