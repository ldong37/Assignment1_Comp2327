import unittest
from email_validator import validate_email, EmailNotValidError
from account.client import client

class TestClient(unittest.TestCase):
    #__init__ method tests
    def test_account_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            client(-1, "Test", "test@example.com")
        self.assertEqual(str(context.exception), "Client ID must be a positive number.")

    def test_account_id_is_zero(self):
        with self.assertRaises(ValueError) as context:
            client(0, "Test", "test@example.com")
        self.assertEqual(str(context.exception), "Client ID must be a positive number.")

    def test_name_is_empty(self):
        with self.assertRaises(ValueError) as context:
            client(1, "   ", "test@example.com")
        self.assertEqual(str(context.exception), "Name cannot be empty.")

    def test_email_is_invalid(self):
        with self.assertRaises(EmailNotValidError):
            client(1, "Test", "Invalid-email")

    def test_init_valid_instance(self):
        client_instance = client(1, "Test Name", "test@example.com")
        self.assertEqual(client_instance._client_id, 1)
        self.assertEqual(client_instance.name, "Test Name")
        self.assertEqual(client_instance.email_address, "test@example.com")