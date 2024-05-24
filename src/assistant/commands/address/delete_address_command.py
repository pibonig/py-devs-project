from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_address_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: delete_address <name>")
    name = args[0]
    contact = contact_book.get_contact(name)
    if contact:
        contact.delete_address()
        return StringResponse('Contact has been deleted')
    else:
        raise KeyError
