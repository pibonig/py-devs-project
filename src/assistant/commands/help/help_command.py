from src.assistant.commands.contact.add_contact_command import AddContactCommand
from src.assistant.commands.note.add_note_command import AddNoteCommand
from src.assistant.commands.note.add_tag_command import AddTagCommand
from src.assistant.commands.note.change_note_command import ChangeNoteCommand
from src.assistant.commands.note.delete_note_command import DeleteNoteCommand
from src.assistant.commands.note.delete_tag_command import DeleteTagCommand
from src.assistant.commands.note.get_all_notes_command import GetAllNotesCommand
from src.assistant.commands.note.get_note_command import GetNoteCommand
from src.assistant.commands.note.get_tag_command import GetTagCommand
from src.assistant.commands.note.sort_by_tags_command import SortByTagsCommand

from src.response.table_response import TableResponse


def help_command():
    commands_info = [
        ["Command", "Parameters", "Description"],
        ["close, exit", "", "Exit the bot"],
        ["hello", "", "Say hello"],
        ["add_address", "[Name] [Address]", "Add address to contact"],
        ["change_address", "[Name] [Address]", "Change contact address"],
        ["delete_address", "[Name] [Address]", "Delete contact address"],
        ["add_birthday", "[Name] [Birthday]", "Add birthday to contact"],
        ["change_birthday", "[Name] [Birthday]", "Change contact birthday"],
        ["delete_birthday", "[Name] [Birthday]", "Delete contact birthday"],
        ["get_all_birthdays", "", "Get all birthdays"],
        ["get_birthday", "[Name] [Birthday]", "Get contact birthday"],
        [AddContactCommand.name, AddContactCommand.signature, AddContactCommand.description],
        ["delete_contact", "[Name]", "Delete a contact"],
        ["get_all_contacts", "", "Get all contacts"],
        ["get_contact", "[Name]", "Get contact details"],
        ["add_email", "[Name] [Email]", "Add email to contact"],
        ["change_email", "[Name] [Email]", "Change contact email"],
        ["delete_email", "[Name] [Email]", "Delete contact email"],
        [AddNoteCommand.name, AddNoteCommand.signature, AddNoteCommand.description],
        [ChangeNoteCommand.name, ChangeNoteCommand.signature, ChangeNoteCommand.description],
        [DeleteNoteCommand.name, DeleteNoteCommand.signature, DeleteNoteCommand.description],
        [GetAllNotesCommand.name, GetAllNotesCommand.signature, GetAllNotesCommand.description],
        [GetNoteCommand.name, GetNoteCommand.signature, GetNoteCommand.description],
        ["add_phone", "[Name] [Phone]", "Add phone to contact"],
        ["change_phone", "[Name] [Phone]", "Change contact phone"],
        ["delete_phone", "[Name] [Phone]", "Delete contact phone"],
        [AddTagCommand.name, AddTagCommand.signature, AddTagCommand.description],
        [DeleteTagCommand.name, DeleteTagCommand.signature, DeleteTagCommand.description],
        [GetTagCommand.name, GetTagCommand.signature, GetTagCommand.description],
        [SortByTagsCommand.name, SortByTagsCommand.signature, SortByTagsCommand.description],
    ]

    headers = commands_info[0]
    body = commands_info[1:]
    return TableResponse(headers, body)
