from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def get_birthdays(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: get_birthday <days>")
    days = args
    if not contact_book.data:
        return StringResponse("Address book is empty.")
    else:
        result = ''
        book_birthday = contact_book.get_upcoming_birthdays(days)
        if len(book_birthday) > 0:
            for name, birthday in book_birthday.items():
                result += f'Name: {name}, Birthday: {birthday}' + "\n"
            return StringResponse(result)
        else:
            raise KeyError("There are no birthdays in the period")
