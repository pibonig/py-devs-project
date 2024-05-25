from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


class GetAllContactsCommand:
    name = "get_all_contacts"
    signature = ""
    description = "Get all contacts"

    @input_error
    def execute(self, contact_book: ContactBook):
        return str(contact_book)
