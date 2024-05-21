from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def close_command(contact_book: ContactBook):
    # TODO: save book
    pass
