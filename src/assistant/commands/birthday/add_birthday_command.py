from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.birthday import Birthday



@input_error
def add_birthday_command(args: list, contact_book: ContactBook):
    name, date = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        birthday = Birthday(date)
        contact.set_birthday(birthday)
        return 'Birthday has been added to the contact'
