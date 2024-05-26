from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook


class DeleteBirthdayCommand:
    name = "delete_birthday"
    signature = "<name>"
    description = "Delete the birthday of a contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)
        
        name, *_ = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError(f"Contact '{name}' not found")
        else:
            contact.delete_birthday()
            return Fore.GREEN + f"Birthday has been deleted for the contact '{name}'"
