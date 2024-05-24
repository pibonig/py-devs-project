from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def get_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if not args:
        raise ValueError("No search query provided. Example search_note <title>")
    title = ''.join(args)
    result = notebook.get_note(title)

    if result:
        return StringResponse(str(result))
    else:
        raise ValueError(f"Note with title '{title}' not found")