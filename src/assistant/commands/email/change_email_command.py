from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.email import Email

class ChangeEmailCommand:
    name = "change_email"
    signature = "<name> <email>"
    description = "Change contact email"

    @input_error
    def execute(self, args: list, contact_book: ContactBook) :
        if len(args) < 2:
            raise InvalidCommandParamsException(self)
        
        name, email, *_ = args
        record = contact_book.get_contact(name)
        
        if record is None:
            raise KeyError
        else:
            email = Email(email)
            record.set_email(email)
            return "Email has been changed in the contact"
