from tabulate import tabulate


class TableResponse:
    def __init__(self, headers: list, body: list[list]):
        self.headers = headers
        self.body = body

    def __repr__(self):
        return tabulate(self.body, self.headers, tablefmt="grid")
