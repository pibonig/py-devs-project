from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def change_phone_command(args: list, contact_book: ContactBook):
    name, old_phone, new_phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        return 'Contact does not exist'
    else:
        for i, phone in enumerate(contact.phones):
            if phone == old_phone:
                contact.phones[i] = new_phone
        return 'Phone has been changed in the contact'

