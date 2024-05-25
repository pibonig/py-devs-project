from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.note import Note
from src.models.notebook.notebook import Notebook




class AddNoteCommand:
    name='add_note'
    signature="<title> <content>"
    description='Add a new note'

    @input_error
    def execute(self,args: list, notebook: Notebook):
        if len(args) < 2:
            raise InvalidCommandParamsException(self)

        note_title = args[0]
        note_content = ''.join(args[1:])
        note = Note(title=note_title, content=note_content)
        notebook.add_note(note)
        return "Note added"
