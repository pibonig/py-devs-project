from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse


@input_error
def get_all_notes_command(args: list, notebook: NoteBook) -> BaseResponse:
    notes = notebook.list_notes()
    if isinstance(notes, str):
        return notes
    elif not notes:
        return "No notes available"
    else:
        return "\n".join(str(note) for note in notes)
