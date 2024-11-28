import pytest
from exercise_01 import func

text_orig = 'my string'
text_reg = 'My String'
text_punc = 'my string!'
text_rus = 'my stringстрока'
text_all = 'My, Stringстрока!'


def test_orig():
    assert func(text_orig) == text_orig


def test_reg():
    assert func(text_reg) == text_orig


def test_punc():
    assert func(text_punc) == text_orig


def test_rus():
    assert func(text_rus) == text_orig


def test_all():
    assert func(text_all) == text_orig


if __name__ == '__main__':
    pytest.main()
