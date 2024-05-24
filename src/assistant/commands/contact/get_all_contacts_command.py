from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def get_all_contacts_command(contact_book: ContactBook) -> BaseResponse:
    if not contact_book.data:
        raise KeyError
    else:
        result = ""
        for name, contact in contact_book.data.items():
            result += str(contact) + "\n"
        return StringResponse(result)
