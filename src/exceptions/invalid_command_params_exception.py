from colorama import Fore, Back


class InvalidCommandParamsException(Exception):
    def __init__(self, cls):
        super().__init__(
            Fore.RED + f"Invalid command parameters. {Back.WHITE}{Fore.GREEN}Example: {cls.name} {cls.signature}.")
