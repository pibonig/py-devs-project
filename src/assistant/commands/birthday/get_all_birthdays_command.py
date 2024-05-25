from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact_book import ContactBook


class GetAllBirthdaysCommand:
    name = "get_all_birthdays"
    signature = "<number of days>"
    description = "Show all contacts whose birthdays are a specified number of days from the current date."

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) != 1:
            raise InvalidCommandParamsException(self)
        
        if not contact_book.data:
            return "Address book is empty."
        else:
            days = int(args[0])
            result = contact_book.get_upcoming_birthdays(days)
            if result is None:
                return f"No contacts have birthdays within the next {days} days."
            return result
