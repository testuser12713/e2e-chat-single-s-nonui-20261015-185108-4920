import pytest

from textutils.is_palindrome import is_palindrome


def test_palindrome_sentence():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert is_palindrome("hello") is False


def test_empty_and_symbols():
    assert is_palindrome("") is True
    assert is_palindrome("!?,") is True


def test_type_error():
    with pytest.raises(TypeError):
        is_palindrome(123)  # type: ignore[arg-type]
