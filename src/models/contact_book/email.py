import re

from src.models.field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        match = re.search(pattern, value)
        if match:
            self.__value = value
        else:
            raise ValueError("Invalid email format. Try example@example.example")
