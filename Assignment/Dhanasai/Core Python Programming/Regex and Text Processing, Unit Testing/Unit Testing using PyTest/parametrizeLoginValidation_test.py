import pytest
import re
def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@test.com", True),
        ("admin@domain.org", True),
        ("bad.email", False),
        ("@missinguser.com", False),
        ("user@.com", False),
        ("valid.email123@site.net", True)
    ]
)
def test_email_validation(email, expected):
    assert is_valid_email(email) == expected