from decimal import Decimal
from account.account_status import AccountStatus    
from account.client import Client

class BankAccount: 
    """Represents an account at a financial institution. """
    def __init__(self,
                  account_id: int,
                  balance: Decimal, 
                  owner: Client,
                  status: AccountStatus):
        """Initialize the BankAccount object.

        Args:
            account_id (int): Represents the unique identify of the bank account.
            balance (Decimal): Represents the balance of the bank account.
            owner (Client): Represents the owner of the bank account.
            status (AccountStatus): Represents the status of the bank account.
        """