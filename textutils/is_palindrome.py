from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """Return whether text reads the same reversed, ignoring case and non-alphanumerics."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
