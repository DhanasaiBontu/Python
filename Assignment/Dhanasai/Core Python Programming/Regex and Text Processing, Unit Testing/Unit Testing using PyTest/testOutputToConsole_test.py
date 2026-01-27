def greet(name: str):
    print(f"Hello, {name}!")
def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"
