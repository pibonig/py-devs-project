from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse
from src.models.contact_book.phone import Phone



@input_error
def change_phone_command(args: list, contact_book: ContactBook):
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: change_phone <name> <old phone> <new phone>") 
    name, old_phone, new_phone = args
    contact = contact_book.get_contact(name)
    if contact is None:
        raise KeyError
    else:
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        contact.edit_phone(old_phone, new_phone)
        return StringResponse('Phone has been changed in the contact')

