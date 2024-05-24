from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.phone import Phone



@input_error
def add_phone_command(args: list, contact_book: ContactBook):
    name, phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        phone = Phone(phone)
        contact.add_phone(phone)
        return 'Phone has been added to the contact'
