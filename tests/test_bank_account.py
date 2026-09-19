import unittest
from decimal import Decimal
from account.bank_account import BankAccount, AccountStatus
from account.client import client
from account.account_status import AccountStatus

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up a sample client and bank account for testing."""
        self.client_instance = client(1, "Test Name", "test@example.com")
        self.account = BankAccount(account_id=100, balance=Decimal('1000.00'), owner=self.client_instance, status=AccountStatus.ACTIVE)