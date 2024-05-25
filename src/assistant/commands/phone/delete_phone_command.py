from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.phone import Phone
from colorama import Fore


class DeletePhoneCommand:
    name = "delete_phone"
    signature = "<name> <phone>"
    description = "Delete contact phone"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        name, phone, *_ = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError
        else:
            phone = Phone(phone)
            contact.delete_phone(phone)
            return Fore.GREEN + "Phone has been delete in the contact"
