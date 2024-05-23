from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def add_address_command(args: list, contact_book: ContactBook):
    name, adress = args
    record = contact_book.get_contact(name)
    if record is None:
        return 'Condact does not exist'
    else:
        record.set_address(adress)
        return 'Adress has been added to the contact'
