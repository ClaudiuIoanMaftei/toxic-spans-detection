import pytest

from src.server.postprocessing.merger import Merger

documents = [[1, 2, 3, 4, 8, 9, 10], [5, 6, 7], [11, 12], [15], [14], [13]]
expectedResult = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}


@pytest.fixture
def merged_documents():
    merger = Merger(documents)
    merger.run()
    return merger.get_result()


def test_merging(merged_documents):
    assert merged_documents == expectedResult
