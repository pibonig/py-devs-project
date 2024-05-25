from typing import Optional

from src.models.contact_book.address import Address
from src.models.contact_book.birthday import Birthday
from src.models.contact_book.email import Email
from src.models.contact_book.name import Name
from src.models.contact_book.phone import Phone


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

    def __str__(self):
        email = self.email if self.email else 'not provided'
        birthday = self.birthday if self.birthday else 'not provided'
        address = self.address if self.address else 'not provided'
        phones = '; '.join(p.value for p in self.phones) if self.phones else 'not provided'
        return f"Contact name: {self.name.value}, email: {email}, address: {address}, birthday: {birthday}, phones: {phones}"

    def __repr__(self):
        return f"Contact(name={self.name!r}, phones={self.phones!r}, email={self.email!r}, address={self.address!r}, birthday={self.birthday!r})"
