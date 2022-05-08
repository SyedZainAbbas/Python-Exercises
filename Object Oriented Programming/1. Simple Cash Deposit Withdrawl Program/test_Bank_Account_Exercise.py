import pytest
from Bank_Account_Exercise import BankAccount
from Bank_Account_Exercise import BalanceError

def test_negative_deposit():
    value = '-200'
    with pytest.raises(ValueError):
        tst_1 = BankAccount('tst_1')
        tst_1.deposit(value)

def test_integer_deposit():
    value = '<'
    with pytest.raises(ValueError):
        tst_2 = BankAccount('tst_2')
        tst_2.deposit(value)

def test_negative_withdrawl():
    value = '-200'
    with pytest.raises(ValueError):
        tst_3 = BankAccount('tst_3')
        tst_3.withdrawl(value)

def test_integer_withdrawl():
    value = '<'
    with pytest.raises(ValueError):
        tst_4 = BankAccount('tst_4')
        tst_4.withdrawl(value)

def test_balance_withdrawl():
    deposit = '100'
    withdrawl = '150'
    with pytest.raises(BalanceError):
        tst_5 = BankAccount('tst_5')
        tst_5.deposit(deposit)
        tst_5.withdrawl(withdrawl)