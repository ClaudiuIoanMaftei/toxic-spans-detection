from src.server.postprocessing import PostProcessor


class Merger(PostProcessor):

    def __init__(self, documents):
        super().__init__(documents)
        self.merged_documents = set()

    def merge(self):
        for document in self.documents:
            self.merged_documents = self.merged_documents.union(document)

    def run(self):
        self.merge()

    def get_result(self):
        return self.merged_documents
