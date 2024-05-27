from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook


class GetAllBirthdaysCommand:
    name = "get_all_birthdays"
    signature = ""
    description = "Show birthdays for all contacts."

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) != 0:
            raise InvalidCommandParamsException(self)

        if not contact_book.data:
            raise KeyError("Address book is empty.")
        else:
            result = contact_book.get_upcoming_birthdays(None)
            if result is None:
                return Fore.RED + f"Birthdays not provided for any contacts."
            return result
