from __future__ import annotations


def reverse_words(text: str) -> str:
    """Reverse the order of words in text, collapsing whitespace."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return " ".join(reversed(text.split()))
