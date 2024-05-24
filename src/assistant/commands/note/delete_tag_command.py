from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def delete_tag_command(args: list, notebook: NoteBook) -> BaseResponse:
    if len(args) != 2:
        raise ValueError("Invalid arguments. Example: delete_note <note_title> <tag>")

    note_title = args[0]
    tag = args[1]

    note = notebook.get_note_by_title(note_title)
    if note:
        if note.delete_tag(tag):
            return StringResponse(f"Tag '{tag}' deleted from the note '{note_title}'.")
        else:
            raise ValueError(f"Tag '{tag}' not found in the note '{note_title}'.")
    else:
        raise ValueError(f"Note with title '{note_title}' not found")
