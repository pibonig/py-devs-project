from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook

class DeleteEmailCommand:
    name = "delete_email"
    signature = "<name> <email>"
    description = "Delete contact email"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)
        
        name = args
        contact = contact_book.get_contact(name)
        
        if contact is None:
            raise KeyError
        else:
            contact.delete_email()
            return "Email has been deleted in the contact"
