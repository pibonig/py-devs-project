from src.decorators import input_error
from src.models.notebook.notebook import Notebook


@input_error
def get_all_notes_command(notebook: Notebook):
    notes = notebook.list_notes()
    if isinstance(notes, str):
        return str(notes)
    elif not notes:
        raise ValueError("No notes available")
    else:
        notes_content = "\n".join(str(note) for note in notes)
        return notes_content
