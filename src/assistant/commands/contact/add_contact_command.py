from src.models.contact_book.phone import Phone
from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.contact_book.contact import Contact
from src.models.contact_book.contact_book import ContactBook


class AddContactCommand:
    name = "add_contact"
    signature = "<name> <phone>"
    description = "Add a new contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        name, phone, *_ = args
        contact = contact_book.get_contact(name)

        if contact is None:
            contact = Contact(name)
            contact_book.add_contact(contact)

        phone = Phone(phone)
        contact.add_phone(phone)
        return "Contact updated."
