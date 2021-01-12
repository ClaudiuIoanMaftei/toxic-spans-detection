import pytest

from src.server.core.dl.parsing.tokenator import Tokenator


def test_null_input():
    vocab = Tokenator.tokenate("")
    vocab_spaces = Tokenator.tokenate("     ")
    assert(vocab.get_tokens() == {})
    assert(vocab_spaces.get_tokens() == {})


def test_single_word():
    vocab = Tokenator.tokenate("test")
    assert(vocab.get_tokens() == {1: 'test'})


def test_multiple_words():
    vocab = Tokenator.tokenate("this comm!ent is not toxic at all")
    assert(vocab.get_tokens() == {
        1: 'this',
        2: 'comm!ent',
        3: 'is',
        4: 'not',
        5: 'toxic',
        6: 'at',
        7: 'all'
    })


def test_repetitive_words():
    vocab = Tokenator.tokenate("this comment, is a comment indeed.")
    assert(vocab.get_tokens() == {
        1: 'this',
        2: 'comment',
        3: 'is',
        4: 'a',
        5: 'indeed'
    })
