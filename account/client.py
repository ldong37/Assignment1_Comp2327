from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self,
                 client_id: str,
                 name: str,
                 email_address: str):
        