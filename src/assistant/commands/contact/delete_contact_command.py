from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def delete_contact_command(args: list, contact_book: ContactBook):
    name = args[0]      
    contact = contact_book.get_contact(name)
    if contact:
        contact_book.delete_contact(name)
    else:
        raise KeyError
