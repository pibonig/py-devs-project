from src.decorators import input_error
from src.models.notebook.notebook import Notebook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException

class ChangeTagCommand:
    name = "change_tag"
    signature = "<note_title> <old_tag> <new_tag>"
    description = "Edit tag of a note"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if len(args) != 3:
            raise InvalidCommandParamsException(self)

        note_title, old_tag, new_tag = args[0], args[1], args[2]

        note = notebook.get_note_by_title(note_title)
        if note:
            if old_tag in note.tags:
                note.delete_tag(old_tag)
                note.add_tag(new_tag)
                return f"Tag '{old_tag}' edited to '{new_tag}' in the note '{note_title}'."
            else:
                raise ValueError(f"Tag '{old_tag}' not found in the note '{note_title}'.")
        else:
            raise KeyError(f"Note with title '{note_title}' not found")