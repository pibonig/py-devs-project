from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse



@input_error
def delete_phone_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        contact.delete_phone(phone)
        return StringResponse('Phone has been delete in the contact')
