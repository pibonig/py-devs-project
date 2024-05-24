from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def get_all_notes_command(args: list, notebook: NoteBook) -> BaseResponse:
    notes = notebook.list_notes()
    if isinstance(notes, str):
        return notes
    elif not notes:
        raise ValueError("No notes available") 
    else:
        notes_content="\n".join(str(note) for note in notes)
        return StringResponse(notes_content)
