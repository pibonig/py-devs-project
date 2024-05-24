from src.response.string_response import StringResponse


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return StringResponse(str(self.value))
