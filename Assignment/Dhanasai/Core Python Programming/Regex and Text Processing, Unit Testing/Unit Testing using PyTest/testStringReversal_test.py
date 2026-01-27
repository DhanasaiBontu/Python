def reverse(s: str) -> str:
    return s[::-1]
def test_reverse_hello():
    assert reverse("hello") == "olleh"
def test_reverse_abc():
    assert reverse("abc") == "cba"