from src.decorators import input_error
from src.models.notebook.notebook import Notebook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException


class GetTagCommand:
    name = "get_tag"
    signature = "<tag>"
    description = "Retrieve notes with a specific tag"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if not args:
            raise InvalidCommandParamsException(self)

        tag = ''.join(args)
        matching_notes = []
        for note in notebook.notes:
            if tag in note.tags:
                matching_notes.append(note)

        if matching_notes:
            notes_content = "\n".join(str(note) for note in matching_notes)
            return notes_content
        else:
            raise ValueError(f"No notes found with tag '{tag}'")
