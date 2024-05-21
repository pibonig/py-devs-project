from dataclasses import dataclass

from src.models.notebook.note import Note


@dataclass
class NoteBook:
    notes: list[Note]

    def add_note(self, note: Note):
        pass

    def get_note(self):
        pass

    def delete_note(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
