from datetime import datetime

from src.models.field import Field
from src.response.string_response import StringResponse


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        try:
            self.__value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __repr__(self):
        return StringResponse(self.__value.strftime("%d.%m.%Y"))
