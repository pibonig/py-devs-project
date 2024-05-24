from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse



@input_error
def delete_contact_command(args: list, contact_book: ContactBook):
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: delete_contact <name>") 
    name = args[0]      
    contact = contact_book.get_contact(name)
    if contact:
        contact_book.delete_contact(name)
        return StringResponse('Contact has been deleted')
    else:
        raise KeyError
