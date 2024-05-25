from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class ChangeNoteCommand:
    name = "change_note"
    signature = "<note_title> <content>"
    description = "Change the content of an existing note"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        note_title = args[0]
        new_content = ' '.join(args[1:])
        note = notebook.get_note_by_title(note_title)

        if note:
            note.change(new_content)
            return Fore.GREEN + f"Note '{note_title}' updated to: {new_content}"
        else:
            raise KeyError(f"Note with title '{note_title}' not found")
