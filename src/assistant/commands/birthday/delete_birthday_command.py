from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_birthday_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: delete_birthday <name>")
    name = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        contact.delete_birthday()
        return StringResponse('Birthday has been deleted in the contact')
