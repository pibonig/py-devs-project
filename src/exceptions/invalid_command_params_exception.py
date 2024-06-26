from colorama import Fore


class InvalidCommandParamsException(Exception):
    def __init__(self, cls):
        super().__init__(
            Fore.RED + f"Invalid command parameters. {Fore.WHITE}Example: {cls.name} {cls.signature}.")
