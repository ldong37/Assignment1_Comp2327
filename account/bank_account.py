from decimal import Decimal
from account.account_status import AccountStatus    
from account.client import client

class BankAccount: 
    """Represents an account at a financial institution. """
    def __init__(self,
                  account_id: int,
                  balance: Decimal, 
                  owner: client,
                  status: AccountStatus):
        """Initialize the BankAccount object.

        Args:
            account_id (int): Represents the unique identify of the bank account.
            balance (Decimal): Represents the balance of the bank account.
            owner (Client): Represents the owner of the bank account.
            status (AccountStatus): Represents the status of the bank account.
        """

        if account_id <= 0:
            raise ValueError("Account ID must be a positive number.")
        self._account_id = account_id
        self._balance = balance
        self._owner = owner
        self._status = status

@property
def account_id(self) -> int:
    """int: Gets the read-only account ID of the bank account."""
    return self._account_id

@property
def balance(self) -> Decimal:
    """Decimal: Gets the read-only balance of the bank account."""
    return self._balance

@property
def owner(self) -> client:
    """Client: Gets the read-only owner of the bank account."""
    return self._owner

@property
def status(self) -> AccountStatus:
    """AccountStatus: Gets the read-only status of the bank account."""
    return self._status

def _update_balance(self, amount: Decimal) -> None:
    """Updates the balance of the bank account.

    Args:
        amount (Decimal): The amount to update the balance by. Can be positive or negative.
    """
    self._balance += amount

def deposit(self, amount: Decimal) -> None:
    """Deposits an amount into the bank account.

    Args:
        amount (Decimal): The amount to deposit. Must be positive.

    Raises:
        ValueError: If the amount is not positive.
    """
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    self._update_balance(amount)