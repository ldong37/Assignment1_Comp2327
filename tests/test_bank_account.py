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
        self.assertEqual(self.account._account_id, 100)

    def test_balance_property(self):
        self.assertEqual(self.account._balance, Decimal('1000.00'))

    def test_owner_property(self):
        self.assertEqual(self.account._owner, self.client_instance)

    def test_status_property(self):
        self.assertEqual(self.account._status, AccountStatus.ACTIVE)


#Update balance tests
def test_update_balance_positive(self):
    self.account.update_balance(Decimal("1050"))
    self.assertEqual(self.account._BankAccount__balance,Decimal("1050"))

def test_update_balance_negative(self):
    self.account.update_balance(Decimal("-1050"))
    self.assertEqual(self.account._BankAccount__balance,Decimal("-1050"))


