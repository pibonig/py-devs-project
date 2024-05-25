from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.phone import Phone

class ChangePhoneCommand:
    name = "change_phone"
    signature = "<name> <old_phone> <new_phone>"
    description = "Change contact phone"

    @input_error
    def change_phone_command(self, args: list, contact_book: ContactBook) :
        if len(args) < 3:
            raise InvalidCommandParamsException(self)
        
        name, old_phone, new_phone = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError
        else:
            old_phone = Phone(old_phone)
            new_phone = Phone(new_phone)
            contact.edit_phone(old_phone, new_phone)
            return "Phone has been changed in the contact"
