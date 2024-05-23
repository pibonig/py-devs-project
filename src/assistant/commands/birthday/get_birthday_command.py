from src.decorators import input_error
from src.models.contact_book.contact_book import ContactBook


@input_error
def get_birthdays(args: list, contact_book: ContactBook):
    days = args
    if not contact_book.data:
        return "Address book is empty."
    else:
        result = ''
        book_birthday = contact_book.get_upcoming_birthdays(days)
        if len(book_birthday) > 0:
            for name, birthday in book_birthday.items():
                result += f'Name: {name}, Birthday: {birthday}' + "\n"
            return result
        else:
            return 'There are no birthdays in the period'
