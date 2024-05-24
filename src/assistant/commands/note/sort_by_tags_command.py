from src.models.notebook.notebook import NoteBook
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


def sort_by_tags(args: list, notebook: NoteBook) -> BaseResponse:
    if not args:
        raise ValueError("No sort query provided. Example sort_by_tags <tag>")

    tag = ' '.join(args)
    matching_notes = []

    for note in notebook.notes:
        if tag in note.tags:
            matching_notes.append(note)
    if matching_notes:

        sorted_notes = sorted(matching_notes, key=lambda note: note.tags.index(tag))

        notes_content = "\n".join(str(note) for note in sorted_notes)
        return StringResponse(notes_content)
    else:
        raise ValueError(f"No notes found with tag '{tag}'")
