from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from colorama import Fore

class DeleteContactCommand:
    name = "delete_contact"
    signature = "<name>"
    description = "Delete the contact"

    @input_error
    def execute(self,args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)
        
        name = args[0]
        contact = contact_book.get_contact(name)

        if contact:
            contact_book.delete_contact(name)
            return Fore.GREEN + "Contact has been deleted"
        else:
            raise KeyError
