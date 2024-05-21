from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def delete_phone_command(args: list, contact_book: ContactBook):
    pass
