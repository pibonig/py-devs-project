from src.decorators import input_error
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.contact_book import ContactBook


@input_error
def change_birthday_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: change_birthday <name> <date>")
    name, date = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        birthday = Birthday(date)
        contact.set_birthday(birthday)
        return "Birthday has been changed in the contact"
