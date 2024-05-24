from src.decorators import input_error
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def change_birthday_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: change_birthday <name> <date>")
    name, date = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        birthday = Birthday(date)
        contact.set_birthday(birthday)
        return StringResponse("Birthday has been changed in the contact")
