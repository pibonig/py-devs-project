from src.decorators import input_error
from src.models.notebook.notebook import Notebook


@input_error
def get_tag_command(args: list, notebook: Notebook):
    if not args:
        raise ValueError("No search query provided. Example get_tag <tag>")

    tag = ''.join(args)
    matching_notes = []
    for note in notebook.notes:
        if tag in note.tags:
            matching_notes.append(note)

    if matching_notes:
        notes_content = "\n".join(str(note) for note in matching_notes)
        return notes_content
    else:
        raise ValueError(f"No notes found with tag '{tag}'")
