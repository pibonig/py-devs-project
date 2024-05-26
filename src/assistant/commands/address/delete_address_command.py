from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook


class DeleteAddressCommand:
    name = "delete_address"
    signature = "<name>"
    description = "Delete contact address"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)

        name = args[0]
        contact = contact_book.get_contact(name)

        if contact:
            contact.delete_address()
            return Fore.GREEN + "Address has been deleted"
        else:
            raise KeyError(f"Contact '{name}' not found")
