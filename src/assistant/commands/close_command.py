from src.decorators import input_error


class CloseCommand:
    name = ["close", "exit"]
    signature = ""
    description = "Exit the bot"

    @input_error
    def execute(self):
        return False
