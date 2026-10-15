from __future__ import annotations

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a URL-friendly ASCII slug."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")
