from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.email import Email
from starlette.responses import StringResponse





@input_error
def change_email_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError
    name, email = args
    record = contact_book.get_contact(name)
    if record is None:
        raise KeyError
    else:
        email = Email(email)
        record.set_email(email)
        return StringResponse('Email has been changed in the contact')

