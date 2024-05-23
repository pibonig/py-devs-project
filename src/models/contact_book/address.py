from src.models.field import Field


class Address(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value
        
