from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse


@input_error
def get_all_contacts_command(contact_book: ContactBook) -> BaseResponse:
    pass
