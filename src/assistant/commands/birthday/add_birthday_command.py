from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.contact_book import ContactBook


class AddBirthdayCommand:
    name = "add_birthday"
    signature = "<name> <date>"
    description = "Add a birthday to a contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)
        name, date = args
        contact = contact_book.get_contact(name)
        if contact is None:
            raise KeyError
        else:
            birthday = Birthday(date)
            contact.set_birthday(birthday)
            return Fore.GREEN + f"Birthday '{date}' has been added to the contact '{name}'"
