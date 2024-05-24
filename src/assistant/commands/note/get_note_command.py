from src.decorators import input_error
from src.models.notebook.notebook import Notebook


@input_error
def get_note_command(args: list, notebook: Notebook):
    if not args:
        raise ValueError("No search query provided. Example search_note <title>")
    title = ''.join(args)
    result = notebook.get_note(title)

    if result:
        return str(result)
    else:
        raise ValueError(f"Note with title '{title}' not found")
