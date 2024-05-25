from colorama import Fore

from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class DeleteNoteCommand:
    name = "delete_note"
    signature = "<note_title>"
    description = "Delete an existing note by title"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if len(args) != 1:
            raise InvalidCommandParamsException(self)

        note_title = args[0]
        deleted_note = notebook.delete_note_by_title(note_title)

        if deleted_note:
            return Fore.GREEN + f"Note deleted: {deleted_note.title}"
        else:
            raise KeyError(f"Note with title '{note_title}' not found")
