import textutils


def test_public_names_importable_and_callable():
    for name in ("slugify", "truncate", "word_count", "is_palindrome", "reverse_words"):
        assert callable(getattr(textutils, name))
        assert name in textutils.__all__
