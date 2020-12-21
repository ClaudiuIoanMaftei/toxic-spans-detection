import pytest

from src.server.core.dl.parsing.vocabulary import Vocabulary


def test_vocabulary_base_creation():
    created_vocab = Vocabulary(["This", "Is", "A", "Test", "String"])
    generated_vocab = Vocabulary.create("This Is A Test String")

    assert(generated_vocab.get_tokens() == created_vocab.get_tokens())
