import pytest

from textutils.truncate import truncate


def test_normal():
    assert truncate("Hello World", 8) == "Hello..."


def test_short_text_unchanged():
    assert truncate("hi", 5) == "hi"
    assert truncate("hello", 5) == "hello"


def test_small_max_len():
    assert truncate("hello", 2) == "he"
    assert truncate("hello", 0) == ""


def test_max_len_three():
    assert truncate("hello", 3) == "..."


def test_negative():
    with pytest.raises(ValueError):
        truncate("x", -1)


def test_type_error():
    with pytest.raises(TypeError):
        truncate(None, 3)
