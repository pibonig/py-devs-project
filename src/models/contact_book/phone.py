from src.models.field import Field
from colorama import Fore

class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError(Fore.RED + "The phone number must consist of 10 digits")
        self.__value = value
