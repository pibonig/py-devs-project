from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def add_tag_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) < 2:
        raise ValueError("Invalid arguments. Example: add_tag <note_title> <tag>")

    note_title = int(args[0])
    tag = args[1]

    note = notebook.get_note(note_title)
    if note:
        note.add_tag(tag)
        return StringResponse(f"Tag '{tag}' added to the note '{note_title}'.")
    else:
        raise KeyError(f"Note with title '{note_title}' not found")