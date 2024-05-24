from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def delete_birthday_command(args: list, contact_book: ContactBook):
    name = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError('Contact does not exist')
    else:
        contact.delete_birthday()
        return 'Birthday has been deleted in the contact'
