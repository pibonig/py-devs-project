from src.response.base_response import BaseResponse


class StringResponse(BaseResponse):
    def __init__(self, string: str):
        self.string = string

    def __repr__(self):
        return self.string
