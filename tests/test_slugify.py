import pytest

from textutils.slugify import slugify


def test_normal():
    assert slugify("  Crème Brûlée  ") == "creme-brulee"
    assert slugify("Hello, World!") == "hello-world"


@pytest.mark.parametrize("text", ["", "!!!", "   "])
def test_empty_or_symbols(text):
    assert slugify(text) == ""


@pytest.mark.parametrize("bad", [None, 1, b"x"])
def test_type_error(bad):
    with pytest.raises(TypeError):
        slugify(bad)
