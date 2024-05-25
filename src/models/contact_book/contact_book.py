from collections import UserDict
from datetime import datetime, timedelta

from src.models.contact_book.contact import Contact
from src.response.table_response import TableResponse


class ContactBook(UserDict[Contact]):
    pickle_file = 'contact_book.pickle'

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
        target_date = current_date + timedelta(days=days)
        current_year = datetime.now().year
        result = []
        for contact in self.data.values():
            if contact.birthday:
                birthday_date_str = contact.birthday.value.strftime("%d.%m.%Y")  # Convert Birthday object to string
                birthday = datetime.strptime(birthday_date_str, "%d.%m.%Y")
                birthday_date = birthday.date().replace(year=current_year)
                if birthday_date < current_date:
                    birthday_date = birthday_date.replace(year=current_year + 1)
                if current_date <= birthday_date <= target_date:
                    row = [contact.name, birthday_date.strftime("%d.%m.%Y")]
                    result.append(row)
        result.sort(key=lambda x: datetime.strptime(x[1], "%d.%m.%Y"))

        if len(result) == 0:
            return None

        return repr(TableResponse(headers, result))

    def __repr__(self):
        headers = ["Name", "Address", "Email", "Phones", "Birthday"]
        table = []
        for contact in self.data.values():
            table.append([
                contact.name,
                contact.address if contact.address else "",
                contact.email if contact.email else "",
                contact.phones if contact.phones else "",
                contact.birthday if contact.birthday else ""
            ])

        return repr(TableResponse(headers, table))
