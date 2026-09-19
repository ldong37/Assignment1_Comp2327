import unittest
from email_validator import validate_email, EmailNotValidError
from account.client import Client

class TestClient(unittest.TestCase):
    #__init__ method tests
    def test_account_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            Client(-1, "Test", "test@example.com")
        self.assertEqual(str(context.exception), "Client ID must be a positive number.")

    def test_account_id_is_zero(self):
        with self.assertRaises(ValueError) as context:
            Client(0, "Test", "test@example.com")
        self.assertEqual(str(context.exception), "Client ID must be a positive number.")

    def test_name_is_empty(self):
        with self.assertRaises(ValueError) as context:
            Client(1, "   ", "test@example.com")
        self.assertEqual(str(context.exception), "Name cannot be empty.")

    def test_email_is_invalid(self):
        with self.assertRaises(EmailNotValidError):
            Client(1, "Test", "Invalid-email")

    def test_init_valid_instance(self):
        client_instance = Client(1, "Test Name", "test@example.com")
        self.assertEqual(client_instance._client_id, 1)
        self.assertEqual(client_instance.name, "Test Name")
        self.assertEqual(client_instance.email_address, "test@example.com")


#Property tests
    
    def test_email_address_property(self):
        client_instance = Client(10, "Test Name", "test@example.com")
        self.assertEqual(client_instance.client_id, 10)

    def test_name_property(self):
        client_instance = Client(10, "Test Name", "test@example.com")
        self.assertEqual(client_instance.name, "Test Name")

    def test_email_address_property_get(self):
        client_instance = Client(10, "Test Name", "test@example.com")
        self.assertEqual(client_instance.email_address, "test@example.com")

    def test_email_address_property_set_valid(self):
        client_instance = Client(10, "Test Name", "test@example.com")
        client_instance.email_address = "newemail@example.com"
        self.assertEqual(client_instance.email_address, "newemail@example.com")

    def test_email_address_property_set_invalid(self):
        client_instance = Client(10, "Test Name", "test@example.com")
        with self.assertRaises(EmailNotValidError):
            client_instance.email_address = "invalid-email"


#_str_ Test 

def test_str_method(self): 
    """Format: <Client ID: {client_id}, Name: {name}, Email: {email_address}>"""
    client_instance = Client(1010, "John Doe", "john.doe@example.com")
    self.assertEqual(str(client_instance), "<Client ID: 1010, Name: John Doe, Email: john.doe@example.com>")

if __name__ == '__main__':
    unittest.main()