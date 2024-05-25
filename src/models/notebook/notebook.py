from dataclasses import dataclass

from src.models.notebook.note import Note
from src.response.table_response import TableResponse


@dataclass
class Notebook:
    pickle_file = 'note_book.pickle'

    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def get_note_by_title(self, title: str) -> Note:
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def delete_note_by_title(self, title: str) -> Note:
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return note
        return None

    def list_notes(self) -> list[Note]:
        return self.notes

    def __repr__(self):
        body = [[note.title, note.value, ', '.join(note.tags)] for note in self.notes] if self.notes else [
            ["", "", ""]]
        return repr(TableResponse(headers=["Title", "Content", "Tags"], body=body))
