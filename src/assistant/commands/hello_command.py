from colorama import Fore

from src.decorators import input_error


class HelloCommand:
    name = "hello"
    signature = ""
    description = "Say hello"

    @input_error
    def execute(self):
        return Fore.YELLOW + "Hello! How can I help you?"
