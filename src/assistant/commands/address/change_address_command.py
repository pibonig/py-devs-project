from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.address import Address
from starlette.responses import StringResponse




@input_error
def change_address_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError
    name, address_value = args
    contact = contact_book.get_contact(name)
    if contact  is None:
        raise KeyError
    else:
        address = Address(address_value)
        contact.set_address(address)
        return StringResponse('Adress has been changed to the contact')
