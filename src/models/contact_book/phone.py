from src.models.field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        # TODO: validate input value here
        pass
