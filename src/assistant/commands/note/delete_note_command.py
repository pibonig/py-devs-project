from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) != 1:
        raise ValueError("Invalid arguments. Example: delete_note <note_title>")
   
    note_title = args[0]
    deleted_note = notebook.delete_note(note_title)

    if deleted_note:
        return StringResponse(f"Note deleted: {deleted_note}")
    else:
        raise KeyError(f"Note with title '{note_title}' not found")
