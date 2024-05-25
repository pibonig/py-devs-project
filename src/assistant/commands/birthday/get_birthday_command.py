from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from colorama import Fore



class GetBirthdaysCommand:
    name = "get_birthdays"
    signature = "<days>"
    description = "Get upcoming birthdays within a specified number of days"

    @input_error
    def get_birthdays(self,args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)
        days = int(args[0])
        if days < 0:
            raise ValueError("Number of days must be a positive integer.")
        
        if not contact_book.data:
            return "Address book is empty."
        else:
            result = ''
            book_birthday = contact_book.get_upcoming_birthdays(days)
            if len(book_birthday) > 0:
                for name, birthday in book_birthday.items():
                    result += f'Name: {name}, Birthday: {birthday}' + "\n"
                return result
            else:
                raise KeyError("There are no birthdays in the period")
