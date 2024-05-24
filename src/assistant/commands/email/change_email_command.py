from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.email import Email
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def change_email_command(args: list, contact_book: ContactBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: change_email <name> <email>")
    name, email = args
    record = contact_book.get_contact(name)
    if record is None:
        raise KeyError
    else:
        email = Email(email)
        record.set_email(email)
        return StringResponse('Email has been changed in the contact')
