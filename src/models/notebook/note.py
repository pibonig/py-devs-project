from src.models.field import Field
from src.response.table_response import TableResponse


class Note(Field):
    def __init__(self, title: str, content: str, tags: str = ""):
        super().__init__(content)
        self.title = title
        self.tags = []

    def change(self, new_content: str):
        self.value = new_content

    def add_tag(self, tags: str):
        new_tags = tags.split()
        for tag in new_tags:
            if tag not in self.tags:
                self.tags.append(tag)

    def delete_tag(self, tag: str) -> bool:
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def __repr__(self):
        headers = ["Title", "Content", "Tags"]
        body = [[self.title, self.value, ', '.join(self.tags)]]
        return repr(TableResponse(headers=headers, body=body))
