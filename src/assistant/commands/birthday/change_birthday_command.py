from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.contact_book import ContactBook


class ChangeBirthdayCommand:
    name = "change_birthday"
    signature = "<name> <date>"
    description = "Change the birthday of a contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        name, date = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError(f"Contact '{name}' not found")
        else:
            birthday = Birthday(date)
            contact.set_birthday(birthday)
            return Fore.GREEN + f"Birthday has been changed to '{date}' for the contact '{name}'"
