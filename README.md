# textutils

Kleine Python-Bibliothek mit fünf unabhängigen String-Hilfsfunktionen. Keine Laufzeit-Abhängigkeiten, nur die Standardbibliothek.

## Tech-Stack

Python 3.10+, pyproject.toml (setuptools), pytest, ruff.

## Installation

```bash
pip install -e '.[dev]'
```

## Entwicklung

```bash
pytest
ruff check .
```

Es gibt keinen Server und keinen Build. Umgebungsvariablen werden nicht benötigt.

## Verwendung

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

## Funktionen

- `slugify(text: str) -> str` – URL-freundlicher Slug
- `truncate(text: str, max_len: int) -> str` – Text kürzen
- `word_count(text: str) -> int` – Wörter zählen
- `is_palindrome(text: str) -> bool` – Palindrom-Prüfung
- `reverse_words(text: str) -> str` – Wortreihenfolge umkehren

Alle Funktionen werfen `TypeError` bei Nicht-String-Eingabe; `truncate` wirft `ValueError` bei negativem `max_len`.
