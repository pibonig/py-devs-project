from dataclasses import dataclass

from src.models.notebook.note import Note


@dataclass
class NoteBook:
    notes: list[Note]

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
    
    def __str__(self):
        note_titles = [note.title for note in self.notes]
        return ", ".join(note_titles)

    def __repr__(self):
        return f"NoteBook(notes={self.notes})"
