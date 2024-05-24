from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.email import Email



@input_error
def add_email_command(args: list, contact_book: ContactBook):
    name, email = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        email = Email(email)
        contact.set_email(email)
        return 'Email has been added to the contact'