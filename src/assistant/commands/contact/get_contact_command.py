from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def get_contact_command(args: list, contact_book: ContactBook):
    if len(args) < 1:
        raise ValueError("No content provided for the note. Example: get_contact <name>")
    name = args[0]
    contact = contact_book.get_contact(name)
    if contact:
        return contact
    else:
        raise KeyError
