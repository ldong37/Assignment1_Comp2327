from email_validator import validate_email, EmailNotValidError

class Client:  #Prepresent items in the client section
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

        try:
            validated_email = validate_email(email_address)
        except EmailNotValidError:
            raise ValueError("Invalid email address.")

        self.client_id = client_id
        self.name = client_name
        self.email_address = validated_email.email

        #Validate and normalize the email by using setter method
        self.email_address = validated_email.email