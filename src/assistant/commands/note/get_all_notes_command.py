from src.decorators import input_error
from src.models.notebook.notebook import Notebook
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException

class GetAllNotesCommand:
    name = "get_all_notes"
    signature = ""
    description = "Get all notes"


    @input_error
    def execute(self, args:list,notebook: Notebook):
        if args:
            raise InvalidCommandParamsException(self)
    
        notes = notebook.list_notes()
        if isinstance(notes, str):
            return notes
        elif not notes:
            raise ValueError("No notes available")
        else:
            notes_content = "\n".join(str(note) for note in notes)
            return notes_content
