from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.contact import Contact


@input_error
def add_contact_command(args: list, contact_book: ContactBook):    
    name, phone, *_ = args
    contact = contact_book.get_contact(name)
    if contact is None:
        contact = Contact(name)
        contact_book.add_contact(contact)
    contact.add_phone(phone)
    return "Contact updated."
    
