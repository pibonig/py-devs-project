from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class GetAllNotesCommand:
    name = "get_all_notes"
    signature = ""
    description = "Get all notes"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if args:
            raise InvalidCommandParamsException(self)

        return repr(notebook)
