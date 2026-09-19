import unittest
from decimal import Decimal
from account.bank_account import BankAccount
from account.client import Client
from account.account_status import AccountStatus

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up a sample client and bank account for testing."""
        self.client_instance = Client(1, "Test Name", "test@example.com")
        self.account = BankAccount(account_id=100, balance=Decimal('1000.00'), owner=self.client_instance, status=AccountStatus.ACTIVE)


#__init__ method tests

    def test_account_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(-1, Decimal('1000.00'), self.client_instance, AccountStatus.ACTIVE)
        self.assertEqual(str(context.exception), "account_id must be a value greater than zero")

    def test_account_id_is_zero(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(0, Decimal('1000.00'), self.client_instance, AccountStatus.ACTIVE)
        self.assertEqual(str(context.exception), "account_id must be a value greater than zero")

    def test_init_valid_instance(self):
        self.assertEqual(self.account._BankAccount_account_id, 100)
        self.assertEqual(self.account._BankAccount_balance, Decimal('1000.00'))


#Property tests
    
    def test_account_id_property(self):
        self.assertEqual(self.account._account_id, 101)

    def test_balance_property(self):
        self.assertEqual(self.account._balance, Decimal('1000.00'))

    def test_owner_property(self):
        self.assertEqual(self.account._owner, self.client_instance)

    def test_status_property(self):
        self.assertEqual(self.account._status, AccountStatus.ACTIVE)


#Update balance tests
def test_update_balance_positive(self):
    self.account.update_balance(Decimal("50"))
    self.assertEqual(self.account._BankAccount__balance,Decimal("1050"))

def test_update_balance_negative(self):
    self.account.update_balance(Decimal("-50"))
    self.assertEqual(self.account.balance,Decimal("950"))


#Deposit tests
def test_deposit_less_than_zero(self):
    with self.assertRaises(ValueError) as context:
         self.account.deposit(Decimal("-10.00"))
    self.assertEqual(str(context.exception), "amount must be a value greater than or equal to zero")

def test_deposit_valid(self):
    self.account.deposit(Decimal("250.00"))
    self.assertEqual(self.account.balance,Decimal("1250.00"))


#Withdraw tests

def test_withdraw_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(Decimal("-10.00"))
        self.assertEqual(str(context.exception), "amount must be a value greater than or equal to zero")

def test_withdraw_zero(self):
        # Zero is allowed by the logic, but it shouldn't change the balance
        self.account.withdraw(Decimal("0.00"))
        self.assertEqual(self.account.balance, Decimal("1000.00"))

def test_withdraw_greater_than_balance(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(Decimal("1500.00"))
        self.assertEqual(str(context.exception), "amount cannot exceed the account balance")

def test_withdraw_valid(self):
        self.account.withdraw(Decimal("200.00"))
        self.assertEqual(self.account.balance, Decimal("800.00"))


#_str_ test

def test_str_representation(self):
     #Base on the ex:Account num:2026 Balance : $6,764.64
     #Client account starts at 1000.00, so it should format to $1,000.00
     self.assertEqual(str(self.account),"Account Number: 101 Balance: $1,000.00")

if __name__ == '__main__':
    unittest.main()