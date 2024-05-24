from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def change_email_command(args: list, contact_book: ContactBook):
    name, email = args
    record = contact_book.get_contact(name)
    if record is None:
        raise KeyError('Contact does not exist')
    else:
        record.set_email(email)
        return 'Email has been changed in the contact'

