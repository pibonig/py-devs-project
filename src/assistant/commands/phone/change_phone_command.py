from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse



@input_error
def change_phone_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError
    name, old_phone, new_phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        for i, phone in enumerate(contact.phones):
            if phone == old_phone:
                contact.phones[i] = new_phone
        return StringResponse('Phone has been changed in the contact')

