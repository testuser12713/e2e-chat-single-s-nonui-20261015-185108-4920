import pytest

from textutils.reverse_words import reverse_words


def test_normal():
    assert reverse_words("a b c") == "c b a"


def test_whitespace_collapsing():
    assert reverse_words("  one two   three ") == "three two one"


def test_empty():
    assert reverse_words("") == ""


@pytest.mark.parametrize("bad", [None, 1, b"x", ["a"]])
def test_type_error(bad):
    with pytest.raises(TypeError):
        reverse_words(bad)
