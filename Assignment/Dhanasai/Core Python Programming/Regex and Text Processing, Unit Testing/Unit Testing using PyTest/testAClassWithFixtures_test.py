import pytest
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
@pytest.fixture
def account():
    """Provides a fresh BankAccount with 100 balance before each test"""
    return BankAccount(100)
def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150
def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70
def test_deposit_and_withdraw(account):
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
def test_withdraw_more_than_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(200)
def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-10)
def test_negative_withdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(-5)