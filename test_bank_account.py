import pytest
from bank_account import BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.balance == 100

def test_deposit_valid():
    account = BankAccount(0)
    account.deposit(50)
    assert account.balance == 50

def test_withdraw_valid():
    account = BankAccount(100)
    account.withdraw(40)
    assert account.balance == 60

def test_deposit_negative_raises_error():
    account = BankAccount(50)
    with pytest.raises(ValueError, match="Сума поповнення має бути більшою за нуль"):
        account.deposit(-10)

def test_withdraw_insufficient_funds():
    account = BankAccount(50)
    with pytest.raises(ValueError, match="Недостатньо коштів на рахунку"):
        account.withdraw(100)

def test_initial_balance_negative_raises_error():
    with pytest.raises(ValueError):
        BankAccount(-10)