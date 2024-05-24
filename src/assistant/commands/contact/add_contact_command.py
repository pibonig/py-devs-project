from src.decorators import input_error
from src.models.contact_book.contact import Contact
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def add_contact_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: add_contact <name> <phone>")
    name, phone, *_ = args
    contact = contact_book.get_contact(name)
    if contact is None:
        contact = Contact(name)
        contact_book.add_contact(contact)
    contact.add_phone(phone)
    return StringResponse("Contact updated.")
