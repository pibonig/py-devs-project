from typing import Optional

from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from src.models.contact_book.name import Name
from src.models.contact_book.phone import Phone
from src.response.table_response import TableResponse


class Contact:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.address: Optional[Address] = None
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        for contact_phone in self.phones:
            if str(contact_phone) == str(phone):
                self.phones.remove(contact_phone)
                return
        raise ValueError("Phone number not found")

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if str(phone) == str(old_phone):
                phone.value = new_phone.value
                return
        raise ValueError("Phone number not found")

    def get_phones(self):
        return self.phones

    def set_email(self, email: Email):
        self.email = email

    def get_email(self):
        return self.email

    def delete_email(self):
        self.email = None

    def set_address(self, address: Address):
        self.address = address

    def get_address(self):
        return self.address

    def delete_address(self):
        self.address = None

    def set_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def get_birthday(self):
        return self.birthday

    def delete_birthday(self):
        self.birthday = None

    def __repr__(self):
        headers = ["Name", "Address", "Email", "Phones", "Birthday"]
        table = [
            [
                self.name,
                self.address,
                self.email,
                ', '.join(str(phone) for phone in self.phones),
                self.birthday
            ]
        ]

        return repr(TableResponse(headers, table))
