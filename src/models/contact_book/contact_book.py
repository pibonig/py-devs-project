from collections import UserDict
from datetime import datetime, timedelta
from tabulate import tabulate
from src.models.contact_book.contact import Contact


class ContactBook(UserDict[Contact]):
    def add_contact(self, contact: Contact):
        self.data[contact.name.value] = contact

    def get_contact(self, name: str):
        return self.data.get(name)

    def delete_contact(self, name: str):
        if name in self.data:
            self.data.pop(name)
        else:
            raise ValueError("Contact not found.")

    def get_upcoming_birthdays(self, days: int):
        headers = ["Name", "Congratulation date"]
        current_date = datetime.today().date()
        current_timedelta = current_date + timedelta(days)
        current_year = datetime.now().year
        result = []
        for contact in self.data.values():
            if contact.birthday:
                birthday_date = contact.birthday.value.date().replace(year=current_year)
                if birthday_date < current_date:
                    birthday_date = birthday_date.replace(year=current_year + 1)
                if current_date <= birthday_date <= current_timedelta:
                    row =[contact.name, birthday_date.strftime("%d.%m.%Y")]
                    result.append(row)
        result.sort(key=lambda x: datetime.strptime(x[1], "%d.%m.%Y"))
        return tabulate(result, headers, tablefmt="grid")

    def __str__(self):
        headers = ["Name", "Address", "Email", "Phones", "Birthday"]
        table = []
        for contact in self.data.values():
            row = [
                contact.name,
                contact.address if contact.address else "",
                contact.email if contact.email else "",
                contact.phones if contact.phones else "",
                contact.birthday if contact.birthday else ""
            ]
            table.append(row)
        return tabulate(table, headers, tablefmt="grid")

    def __repr__(self):
        return f"ContactBook: {self.data}"

