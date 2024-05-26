from src.response.table_response import TableResponse
from src.decorators import input_error
from src.exceptions.invalid_command_params_exception import InvalidCommandParamsException
from src.models.notebook.notebook import Notebook


class SortByTagsCommand:
    name = "sort_by_tags"
    signature = "<tag>"
    description = "Sort notes by a specific tag"

    @input_error
    def execute(self, args: list, notebook: Notebook):
        if not args:
            raise InvalidCommandParamsException(self)

        tag = ' '.join(args)
        matching_notes = []

        for note in notebook.notes:
            if tag in note.tags:
                matching_notes.append(note)
        if matching_notes:
            headers = ["Title", "Content", "Tags"]
            body = [[note.title, note.value, ', '.join(note.tags)] for note in matching_notes]
            table = TableResponse(headers=headers, body=body)
            return repr(table)
        else:
            raise ValueError(f"No notes found with tag '{tag}'")
