from src.assistant.commands.email.delete_email_command import DeleteEmailCommand
from src.assistant.commands.email.change_email_command import ChangeEmailCommand
from src.assistant.commands.email.add_email_command import AddEmailCommand
from src.assistant.commands.contact.get_contact_command import GetContactCommand
from src.assistant.commands.contact.get_all_contacts_command import GetAllContactsCommand
from src.assistant.commands.contact.delete_contact_command import DeleteContactCommand
from src.assistant.commands.phone.delete_phone_command import DeletePhoneCommand
from src.assistant.commands.phone.change_phone_command import ChangePhoneCommand
from src.assistant.commands.phone.add_phone_command import AddPhoneCommand
from src.assistant.commands.hello_command import HelloCommand
from src.assistant.commands.close_command import CloseCommand
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
        [CloseCommand.name, CloseCommand.signature, CloseCommand.description],
        [HelloCommand.name, HelloCommand.signature, HelloCommand.description],
        ["add_address", "[Name] [Address]", "Add address to contact"],
        ["change_address", "[Name] [Address]", "Change contact address"],
        ["delete_address", "[Name] [Address]", "Delete contact address"],
        ["add_birthday", "[Name] [Birthday]", "Add birthday to contact"],
        ["change_birthday", "[Name] [Birthday]", "Change contact birthday"],
        ["delete_birthday", "[Name] [Birthday]", "Delete contact birthday"],
        ["get_all_birthdays", "", "Get all birthdays"],
        ["get_birthday", "[Name] [Birthday]", "Get contact birthday"],
        [AddContactCommand.name, AddContactCommand.signature, AddContactCommand.description],
        [DeleteContactCommand.name, DeleteContactCommand.signature, DeleteContactCommand.description],
        [GetAllContactsCommand.name, GetAllContactsCommand.signature, GetAllContactsCommand.description],
        [GetContactCommand.name, GetContactCommand.signature, GetContactCommand.description],
        [AddEmailCommand.name, AddEmailCommand.signature, AddEmailCommand.description],
        [ChangeEmailCommand.name, ChangeEmailCommand.signature, ChangeEmailCommand.description],
        [DeleteEmailCommand.name, DeleteEmailCommand.signature, DeleteEmailCommand.description],
        [AddNoteCommand.name, AddNoteCommand.signature, AddNoteCommand.description],
        [ChangeNoteCommand.name, ChangeNoteCommand.signature, ChangeNoteCommand.description],
        [DeleteNoteCommand.name, DeleteNoteCommand.signature, DeleteNoteCommand.description],
        [GetAllNotesCommand.name, GetAllNotesCommand.signature, GetAllNotesCommand.description],
        [GetNoteCommand.name, GetNoteCommand.signature, GetNoteCommand.description],
        [AddPhoneCommand.name, AddPhoneCommand.signature, AddPhoneCommand.description],
        [ChangePhoneCommand.name, ChangePhoneCommand.signature, ChangePhoneCommand.description],
        [DeletePhoneCommand.name, DeletePhoneCommand.signature, DeletePhoneCommand.description],
        [AddTagCommand.name, AddTagCommand.signature, AddTagCommand.description],
        [DeleteTagCommand.name, DeleteTagCommand.signature, DeleteTagCommand.description],
        [GetTagCommand.name, GetTagCommand.signature, GetTagCommand.description],
        [SortByTagsCommand.name, SortByTagsCommand.signature, SortByTagsCommand.description],
    ]

    headers = commands_info[0]
    body = commands_info[1:]
    return TableResponse(headers, body)
