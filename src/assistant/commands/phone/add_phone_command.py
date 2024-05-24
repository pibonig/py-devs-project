from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.phone import Phone
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def add_phone_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: add_phone <name> <phone>")
    name, phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        phone = Phone(phone)
        contact.add_phone(phone)
        return StringResponse("Phone has been added to the contact")
