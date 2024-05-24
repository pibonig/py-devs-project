from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook
from starlette.responses import StringResponse



@input_error
def show_birthdays_command(contact_book: ContactBook):
    if not contact_book.data:
        return StringResponse("Address book is empty.")
    else:
        result = ''
        for name, contact in contact_book.items():
            result += f'Name: {contact.name}, Birthday: {contact.birthday}' + "\n"
        return StringResponse(result)
