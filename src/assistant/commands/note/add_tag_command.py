from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class AddTagCommand:
    name = "add_tag"
    signature = "<note_title> <tag>"
    description = "Add tag to note"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        note_title = args[0]
        tag = " ".join(args[1:])

        note = notebook.get_note_by_title(note_title)
        if note:
            note.add_tag(tag)
            return Fore.GREEN + f"Tag '{tag}' added to the note '{note_title}'."
        else:
            raise KeyError(f"Note with title '{note_title}' not found")
