from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class GetNoteCommand:
    name = "get_note"
    signature = "<title>"
    description = "Retrieve a note by its title"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if not args:
            raise InvalidCommandParamsException(self)
        title = ''.join(args)
        result = notebook.get_note_by_title(title)

        if result:
            return str(result)
        else:
            raise ValueError(f"Note with title '{title}' not found")
