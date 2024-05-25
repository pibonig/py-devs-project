from src.decorators import input_error
from src.models.notebook.notebook import Notebook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException


class DeleteTagCommand:
    name = "delete_tag"
    signature = "<note_title> <tag>"
    description = "Delete a tag from an existing note"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if len(args) != 2:
            raise InvalidCommandParamsException(self)

        note_title = args[0]
        tag = args[1]

        note = notebook.get_note_by_title(note_title)
        if note:
            if note.delete_tag(tag):
                return f"Tag '{tag}' deleted from the note '{note_title}'."
            else:
                raise ValueError(f"Tag '{tag}' not found in the note '{note_title}'.")
        else:
            raise ValueError(f"Note with title '{note_title}' not found")
