from collections import UserDict

from src.models.contact_book.contact import Contact


class ContactBook(UserDict[Contact]):
    def add_contact(self, contact: Contact):
        pass

    def get_contact(self, name: str):
        pass

    def delete_contact(self, name: str):
        pass

    def get_upcoming_birthdays(self, days: int):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
