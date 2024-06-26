from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.email import Email


class AddEmailCommand:
    name = "add_email"
    signature = "<name> <email>"
    description = "Add email to contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        name, email, *_ = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError(f"Contact '{name}' not found")
        else:
            email = Email(email)
            contact.set_email(email)
            return Fore.GREEN + "Email has been added to the contact"
