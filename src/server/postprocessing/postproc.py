from abc import ABC, abstractmethod

class Postprocessor:
    def __init__(self, documents):
        self.documents = documents
        pass

    @abstractmethod
    def run(self):
        pass


if __name__ == "__main__":
    print("Postprocessing")