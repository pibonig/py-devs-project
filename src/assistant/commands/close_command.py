import sys

from lib.storage import Storage
from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def close_command(contact_book: ContactBook):
    Storage.save(contact_book)
    print("Good bye!")
    sys.exit(1)
