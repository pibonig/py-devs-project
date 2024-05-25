from src.decorators import input_error
from src.models.notebook.notebook import Notebook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException


class AddTagCommand:
    name = "add_tag"
    signature = "<note_title> <tag>"
    description = "Add tag to note"

@input_error
def execute(self,args: list, notebook: Notebook):
    if len(args) < 2:
        raise InvalidCommandParamsException(self)

    note_title = args[0]
    tag = args[1]

    note = notebook.get_note(note_title)
    if note:
        note.add_tag(tag)
        return f"Tag '{tag}' added to the note '{note_title}'."
    else:
        raise KeyError(f"Note with title '{note_title}' not found")
