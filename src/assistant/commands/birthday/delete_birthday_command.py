from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException


class DeleteBirthdayCommand:
    name = "delete_birthday"
    signature = "<name>"
    description = "Delete the birthday of a contact"

    @input_error
    def execute(self, args: list, contact_book: ContactBook):
        if len(args) < 1:
            raise InvalidCommandParamsException(self)
        name = args
        contact = contact_book.get_contact(name)
        if contact is None:
            raise KeyError
        else:
            contact.delete_birthday()
            return f"Birthday has been deleted for the contact '{name}'"
