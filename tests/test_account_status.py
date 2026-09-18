import unittest 
from account.bank_account import BankAccount, AccountStatus

class TestBankAccount(unittest.TestCase):
    def test_enumeration_values(self):
        """Test that the enumeration values of AccountStatus are correct."""
        self.assertEqual(AccountStatus.INACTIVE.value, 0)
        self.assertEqual(AccountStatus.ACTIVE.value, 1)
        self.assertEqual(AccountStatus.SUSPENDED.value, 2)
        self.assertEqual(AccountStatus.CLOSED.value, 3)

if __name__ == '__main__':
    unittest.main()