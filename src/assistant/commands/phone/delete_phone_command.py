from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def delete_phone_command(args: list, contact_book: ContactBook):
    name, phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        return 'Contact does not exist'
    else:
        contact.delete_phone(phone)
        return 'Phone has been delete in the contact'
