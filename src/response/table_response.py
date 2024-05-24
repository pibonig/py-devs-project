from tabulate import tabulate

from src.response.base_response import BaseResponse


class TableResponse(BaseResponse):
    def __init__(self, headers: list, body: list[list]):
        if len(headers) != len(body[0]):
            raise ValueError("Number of headers and columns must be equal")

        self.headers = headers
        self.body = body

    def __repr__(self):
        return tabulate(self.body, self.headers, tablefmt="grid")
