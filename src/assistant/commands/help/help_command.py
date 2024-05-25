from src.assistant.commands.address.delete_address_command import DeleteAddressCommand
from src.assistant.commands.address.change_address_command import ChangeAddressCommand
from src.assistant.commands.address.add_address_command import AddAddressCommand
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
from src.assistant.commands.birthday.add_birthday_command import AddBirthdayCommand
from src.assistant.commands.birthday.change_birthday_command import ChangeBirthdayCommand
from src.assistant.commands.birthday.delete_birthday_command import DeleteBirthdayCommand
from src.assistant.commands.birthday.get_all_birthdays_command import GetAllBirthdaysCommand
from src.assistant.commands.birthday.get_birthday_command import GetBirthdaysCommand

from src.response.table_response import TableResponse



class HelpCommand:
    name = "help"
    signature = ""
    description = "Show available commands and their descriptions"

    def execute(self):
        commands_info = [
            ["Command", "Parameters", "Description"],
            [AddAddressCommand.name, AddAddressCommand.signature, AddAddressCommand.description],
            [AddBirthdayCommand.name, AddBirthdayCommand.signature, AddBirthdayCommand.description],
            [AddContactCommand.name, AddContactCommand.signature, AddContactCommand.description],
            [AddEmailCommand.name, AddEmailCommand.signature, AddEmailCommand.description],
            [AddNoteCommand.name, AddNoteCommand.signature, AddNoteCommand.description],
            [AddPhoneCommand.name, AddPhoneCommand.signature, AddPhoneCommand.description],
            [AddTagCommand.name, AddTagCommand.signature, AddTagCommand.description],
            [ChangeAddressCommand.name, ChangeAddressCommand.signature, ChangeAddressCommand.description],
            [ChangeBirthdayCommand.name, ChangeBirthdayCommand.signature, ChangeBirthdayCommand.description],
            [ChangeEmailCommand.name, ChangeEmailCommand.signature, ChangeEmailCommand.description],
            [ChangeNoteCommand.name, ChangeNoteCommand.signature, ChangeNoteCommand.description],
            [ChangePhoneCommand.name, ChangePhoneCommand.signature, ChangePhoneCommand.description],
            [CloseCommand.name, CloseCommand.signature, CloseCommand.description],
            [DeleteAddressCommand.name, DeleteAddressCommand.signature, DeleteAddressCommand.description],
            [DeleteBirthdayCommand.name, DeleteBirthdayCommand.signature, DeleteBirthdayCommand.description],
            [DeleteContactCommand.name, DeleteContactCommand.signature, DeleteContactCommand.description],
            [DeleteEmailCommand.name, DeleteEmailCommand.signature, DeleteEmailCommand.description],
            [DeleteNoteCommand.name, DeleteNoteCommand.signature, DeleteNoteCommand.description],
            [DeletePhoneCommand.name, DeletePhoneCommand.signature, DeletePhoneCommand.description],
            [DeleteTagCommand.name, DeleteTagCommand.signature, DeleteTagCommand.description],
            [GetAllBirthdaysCommand.name, GetAllBirthdaysCommand.signature, GetAllBirthdaysCommand.description],
            [GetAllContactsCommand.name, GetAllContactsCommand.signature, GetAllContactsCommand.description],
            [GetAllNotesCommand.name, GetAllNotesCommand.signature, GetAllNotesCommand.description],
            [GetBirthdaysCommand.name, GetBirthdaysCommand.signature, GetBirthdaysCommand.description],
            [GetContactCommand.name, GetContactCommand.signature, GetContactCommand.description],
            [GetNoteCommand.name, GetNoteCommand.signature, GetNoteCommand.description],
            [GetTagCommand.name, GetTagCommand.signature, GetTagCommand.description],
            [HelloCommand.name, HelloCommand.signature, HelloCommand.description],
            [SortByTagsCommand.name, SortByTagsCommand.signature, SortByTagsCommand.description],
        ]

        headers = commands_info[0]
        body = commands_info[1:]
        return TableResponse(headers, body)
