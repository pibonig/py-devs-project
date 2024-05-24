from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def show_birthdays_command(contact_book: ContactBook) -> BaseResponse:
    if not contact_book.data:
        return StringResponse("Address book is empty.")
    else:
        result = ''
        for name, contact in contact_book.items():
            result += f'Name: {contact.name}, Birthday: {contact.birthday}' + "\n"
        return StringResponse(result)
