from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook


class DeleteEmailCommand:
    name = "delete_email"
    signature = "<name>"
    description = "Delete contact email"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)

        name, *_ = args
        contact = contact_book.get_contact(name)
        if contact is None:
            raise KeyError
        else:
            contact.delete_email()
            return Fore.GREEN + "Email has been deleted in the contact"
