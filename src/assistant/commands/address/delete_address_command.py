from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse


@input_error
def delete_address_command(args: list, contact_book: ContactBook):
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: delete_address <name>") 
    name = args[0]      
    contact  = contact_book.get_contact(name)
    if contact :
        contact.delete_address()
        return StringResponse('Contact has been deleted')
    else:
        raise KeyError