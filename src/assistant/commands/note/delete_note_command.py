from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) != 1:
        raise ValueError("Invalid arguments. Example: delete_note <note>")
    try:
        note_index = int(args[0])
    except ValueError:
        raise "Note index must be an integer."
    deleted_note = notebook.delete_note(note_index)
    if deleted_note:
        return StringResponse(f"Note deleted: {deleted_note}")
    else:
        raise ValueError("Note not found")
