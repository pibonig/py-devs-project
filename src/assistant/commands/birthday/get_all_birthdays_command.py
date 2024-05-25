from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from colorama import Fore

class GetAllBirthdaysCommand:
    name = "get_all_birthdays"
    signature = ""
    description = "Show all contacts with their birthdays"


    @input_error
    def execute(self, args:list, contact_book: ContactBook):
        if args:
            raise InvalidCommandParamsException(self)
        if not contact_book.data:
            return "Address book is empty."
        else:
            result = ''
            for name, contact in contact_book.items():
                result += f'Name: {contact.name}, Birthday: {contact.birthday}' + "\n"
            return result
