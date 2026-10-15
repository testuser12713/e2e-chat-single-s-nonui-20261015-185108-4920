from __future__ import annotations


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return len(text.split())
