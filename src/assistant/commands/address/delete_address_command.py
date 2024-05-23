from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def delete_address_command(args: list, contact_book: ContactBook):
    name = args[0]      
    contact  = contact_book.get_contact(name)
    if contact :
        contact.delete_address()
    else:
        return "Contact not found."