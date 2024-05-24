from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse


@input_error
def get_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if not args:
        raise ValueError("No search query provided. Example search_note <query>")
    query = ''.join(args)
    result = notebook.get_note(query)
    return result if isinstance(result, str) else "\n".join(str(note) for note in result)
