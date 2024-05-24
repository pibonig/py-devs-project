from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.birthday import Birthday
from starlette.responses import StringResponse




@input_error
def add_birthday_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: add_birthday <name> <date>") 
    name, date = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        birthday = Birthday(date)
        contact.set_birthday(birthday)
        return StringResponse('Birthday has been added to the contact')
