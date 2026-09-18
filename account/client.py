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
            raise ValueError("Client ID must be a positive numeber.")