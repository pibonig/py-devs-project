from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.address import Address


@input_error
def add_address_command(args: list, contact_book: ContactBook):
    name, address_value = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        address = Address(address_value)
        contact.set_address(address)
        return 'Adress has been added to the contact'
