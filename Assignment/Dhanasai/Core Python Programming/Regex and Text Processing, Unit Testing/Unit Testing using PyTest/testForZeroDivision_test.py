import pytest
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert str(exc_info.value) == "Cannot divide by zero"