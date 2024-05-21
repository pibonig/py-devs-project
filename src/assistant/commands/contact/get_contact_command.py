from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def get_contact_command(args: list, contact_book: ContactBook):
    pass
