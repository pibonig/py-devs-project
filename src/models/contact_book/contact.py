from typing import Optional

from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from src.models.contact_book.name import Name
from src.models.contact_book.phone import Phone


class Contact:
    name: Name
    phones: list[Phone] = list
    email: Optional[Email] = None
    address: Optional[Address] = None
    birthday: Optional[Birthday] = None

    def __init__(self, name: str):
        self.name = Name(name)

    def add_phone(self, phone: Phone):
        pass

    def delete_phone(self, phone: Phone):
        pass

    def set_email(self, email: Email):
        pass

    def delete_email(self):
        pass

    def set_address(self, address: Address):
        pass

    def delete_address(self):
        pass

    def set_birthday(self, birthday: Birthday):
        pass

    def delete_birthday(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
