from src.decorators import input_error
from src.models.notebook.note import Note
from src.models.notebook.notebook import Notebook


@input_error
def add_note_command(args: list, notebook: Notebook):
    if len(args) < 2:
        raise ValueError("No content provided for the note. Example: add_note <title> <content>")

    note_title = args[0]
    note_content = ''.join(args[1:])
    note = Note(title=note_title, content=note_content)
    notebook.add_note(note)
    return "Note added"
