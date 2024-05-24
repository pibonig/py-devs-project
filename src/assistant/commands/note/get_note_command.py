from src.decorators import input_error
from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def get_note_command(args: list, notebook: NoteBook) -> BaseResponse:
    if not args:
        raise ValueError("No search query provided. Example search_note <query>")
    query = ''.join(args)
    result = notebook.get_note(query)

    if isinstance(result, str):
        raise ValueError(result)
    elif not result:
        raise ValueError('Notes not found')
    elif isinstance(result, list):
        if len(result) == 1:
            return StringResponse(str(result[0]))
        else:
            return StringResponse("\n".join(str(note) for note in result))
    else:
        return StringResponse(str(result))
