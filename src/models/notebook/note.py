from src.models.field import Field


class Note(Field):
    def __init__(self, title: str, content: str):
        super().__init__(content)
        self.title = title
        self.tags = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def delete_tag(self, tag: str) -> bool:
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False
