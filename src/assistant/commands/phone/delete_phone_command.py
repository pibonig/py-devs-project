from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.phone import Phone
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_phone_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: delete_phone <name> <phone>")
    name, phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        phone = Phone(phone)
        contact.delete_phone(phone)
        return StringResponse('Phone has been delete in the contact')
