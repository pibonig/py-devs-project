from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.address import Address
from src.models.contact_book.contact_book import ContactBook

class ChangeAddressCommand:
    name = "change_address"
    signature = "<name> <address>"
    description = "Change contact address"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)
        
        name, address_value, *_ = args
        contact = contact_book.get_contact(name)

        if contact is None:
            raise KeyError
        else:
            address = Address(address_value)
            contact.set_address(address)
            return "Address has been changed to the contact"
