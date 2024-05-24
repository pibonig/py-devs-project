from datetime import datetime
from src.models.contact_book.contact_book import ContactBook
from src.models.contact_book.contact import Contact
from src.assistant.main import start

if __name__ == '__main__':
    # start()
    book = ContactBook()
    contact = Contact('Alex')
    contact.set_birthday('25.05.2000')
    contact2 = Contact('Jo')
    contact2.set_birthday('27.05.2000')
    contact3 = Contact('John')
    book.add_contact(contact)
    book.add_contact(contact2)
    book.add_contact(contact3)
    book.get_upcoming_birthdays(10)
    print(book)
