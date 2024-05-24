from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def change_birthday_command(args: list, contact_book: ContactBook):
    name, date = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError('Contact does not exist')
    else:
        contact.set_birthday(date)
        return 'Birthday has been changed in the contact'
