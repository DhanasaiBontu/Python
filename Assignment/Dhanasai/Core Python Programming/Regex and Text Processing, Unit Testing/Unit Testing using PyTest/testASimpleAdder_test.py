def add(a, b):
    return a + b
def test_add():
    result = add(2, 3)
    print("Checking add function: 2 + 3 =", result) 
    assert result == 5