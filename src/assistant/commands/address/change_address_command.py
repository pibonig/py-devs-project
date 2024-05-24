from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def change_address_command(args: list, contact_book: ContactBook):
    name, adress = args
    contact = contact_book.get_contact(name)
    if contact  is None:
        raise KeyError
    else:
        contact.set_address(adress)
        return 'Adress has been changed to the contact'
