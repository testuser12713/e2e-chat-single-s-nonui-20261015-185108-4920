from __future__ import annotations


def truncate(text: str, max_len: int) -> str:
    """Shorten text to at most max_len characters, ending in '...' when cut."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if len(text) <= max_len:
        return text
    if max_len < 3:
        return text[:max_len]
    return text[: max_len - 3] + "..."
