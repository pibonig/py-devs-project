from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def change_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError('Invalid arguments. Example: edit_note <note_title> <content>')

    note_title = args[0]

    new_content = ''.join(args[1:])
    note = notebook.get_note(note_title)

    if note:
        note.change(new_content)
        return StringResponse(f"Note '{note_title}' updated to: {new_content}")
    else:
        raise KeyError(f"Note with title '{note_title}' not found")
