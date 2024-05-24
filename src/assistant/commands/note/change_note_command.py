from src.decorators import input_error
from src.models.notebook.note import Note
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse


@input_error
def change_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) < 2:
        return 'Invalid arguments. Example: edit_note <content>'
    try:
        note_index = int(args[0])
    except ValueError:
        raise ValueError("Note index must be an integer.")

    new_content = ''.join(args[1:])
    note = notebook.get_note(note_index)

    if isinstance(note, Note):
        note.change(new_content)
        return f"Note updated to: {new_content}"
    else:
        return "Note not found"
