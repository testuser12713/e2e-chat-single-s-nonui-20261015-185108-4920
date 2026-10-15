import pytest

from textutils.word_count import word_count


def test_normal():
    assert word_count("one  two\tthree\nfour") == 4


@pytest.mark.parametrize("text", ["", "   ", "\n\t "])
def test_blank(text):
    assert word_count(text) == 0


@pytest.mark.parametrize("bad", [None, 5, b"a b"])
def test_type_error(bad):
    with pytest.raises(TypeError):
        word_count(bad)
