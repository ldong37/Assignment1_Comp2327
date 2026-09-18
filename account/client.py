from email_validator import validate_email, EmailNotValidError

class client:  #Prepresent items in the client section
    def __init__(self,
                 client_id: str,
                 name: str,
                 email_address: str):

        """Initialize the client object 
          
           Args:
        Client_id (str): Unique identifier for the client.
        Name (str): Name of the client.
        Email_address (str): Email address of the client.
        """

        if client_id <= 0:
            raise ValueError("Client ID must be a positive number.")

        client_name = name.strip()
        if not client_name:
            raise ValueError("Client name cannot be empty.")

        _, parsed_email = parseaddr(email_address)
        if (parsed_email != email_address.strip()
                or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", parsed_email)):
            raise ValueError("Invalid email address.")

        self.client_id = client_id
        self.name = client_name
        self.email_address = parsed_email

    @property
    def client_id(self) -> int:
        """Get the client ID."""
        return self.client_id

    @property
    def name(self) -> str:
        """Get the client name."""
        return self.name

    @property
    def email_address(self) -> str:
        """Get the client email address."""
        return self.email_address

    @email_address.setter
    def email_address(self, value: str) -> None:
        """Set the email address, validating and normalizing it.
           Raises:
           EmailNotValidError: If the email address is not valid. 
        """