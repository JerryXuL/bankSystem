from BankSystem import BankSys
from BankSystem import BankAccount
import pytest

def testcase_create_account():    # test create account function
    newBank = BankSys()
    assert newBank.new_account("jerry", -100) is False
    id = newBank.new_account("jerry", 100)
    assert newBank.accounts[id].balance == 100

def testcase_deposit():    # test deposit function
    newBank = BankSys()
    id = newBank.new_account("jerry", 100)
    assert newBank.deposit(id, 50) is True
    assert newBank.deposit(id, -50) is False
    assert newBank.accounts[id].balance == 150

def testcase_withdraw():   # test withdraw function
    newBank = BankSys()
    id = newBank.new_account("jerry", 100)
    assert newBank.withdraw(id, 50) is True
    assert newBank.withdraw(id, -50) is False
    assert newBank.withdraw(id, 100) is False
    assert newBank.accounts[id].balance == 50

def testcase_transfer():   # test transfer function
    newBank = BankSys()
    id1 = newBank.new_account("jerry", 100)
    id2 = newBank.new_account("Daniel", 200)
    assert newBank.transfer(id1, id2, 120) is False
    assert newBank.transfer(id1, id1, 80) is False
    assert newBank.transfer(id1, id2, 80) is True
    assert newBank.accounts[id1].balance == 20

def testcase_save_and_load():   # test save and load function
    newBank = BankSys()
    id1 = newBank.new_account("jerry", 100)
    id2 = newBank.new_account("Daniel", 200)
    id3 = newBank.new_account("fitz", 2400)
    id4 = newBank.new_account("Lorraine", 1000)
    assert newBank.save_to_csv('bank.csv') is True
    assert newBank.load_from_csv('tesdasd.csv') is False
    assert newBank.load_from_csv('bank.csv') is True
    assert newBank.accounts[id1].balance == 100
    assert newBank.accounts[id2].balance == 200
    assert newBank.accounts[id3].balance == 2400
    assert newBank.accounts[id4].balance == 1000
