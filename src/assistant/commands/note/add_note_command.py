from src.decorators import input_error
from src.models.notebook.note import Note
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse


@input_error
def add_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if not args:
        raise ValueError("No content provided for the note. Example: add_note <content>")

    note_content = ''.join(args)
    note = Note(content=note_content)
    notebook.add_note(note)
    return "Note added"
