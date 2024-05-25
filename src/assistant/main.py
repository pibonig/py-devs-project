import inspect
import sys

from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from lib.storage import Storage
from src.assistant.commands.address.add_address_command import AddAddressCommand
from src.assistant.commands.address.change_address_command import ChangeAddressCommand
from src.assistant.commands.address.delete_address_command import DeleteAddressCommand
from src.assistant.commands.birthday.add_birthday_command import AddBirthdayCommand
from src.assistant.commands.birthday.change_birthday_command import ChangeBirthdayCommand
from src.assistant.commands.birthday.delete_birthday_command import DeleteBirthdayCommand
from src.assistant.commands.birthday.get_all_birthdays_command import GetAllBirthdaysCommand
from src.assistant.commands.birthday.get_birthday_command import GetBirthdaysCommand
from src.assistant.commands.close_command import CloseCommand
from src.assistant.commands.contact.add_contact_command import AddContactCommand
from src.assistant.commands.contact.delete_contact_command import DeleteContactCommand
from src.assistant.commands.contact.get_all_contacts_command import GetAllContactsCommand
from src.assistant.commands.contact.get_contact_command import GetContactCommand
from src.assistant.commands.email.add_email_command import AddEmailCommand
from src.assistant.commands.email.change_email_command import ChangeEmailCommand
from src.assistant.commands.email.delete_email_command import DeleteEmailCommand
from src.assistant.commands.hello_command import HelloCommand
from src.assistant.commands.help.help_command import HelpCommand
from src.assistant.commands.note.add_note_command import AddNoteCommand
from src.assistant.commands.note.add_tag_command import AddTagCommand
from src.assistant.commands.note.change_note_command import ChangeNoteCommand
from src.assistant.commands.note.change_tag_command import ChangeTagCommand
from src.assistant.commands.note.delete_note_command import DeleteNoteCommand
from src.assistant.commands.note.delete_tag_command import DeleteTagCommand
from src.assistant.commands.note.get_all_notes_command import GetAllNotesCommand
from src.assistant.commands.note.get_note_command import GetNoteCommand
from src.assistant.commands.note.get_tag_command import GetTagCommand
from src.assistant.commands.note.sort_by_tags_command import SortByTagsCommand
from src.assistant.commands.phone.add_phone_command import AddPhoneCommand
from src.assistant.commands.phone.change_phone_command import ChangePhoneCommand
from src.assistant.commands.phone.delete_phone_command import DeletePhoneCommand
from src.models.contact_book.contact_book import ContactBook
from src.models.notebook.notebook import Notebook
from src.response.table_response import TableResponse

commands = {
    CloseCommand.name[0]: CloseCommand,
    CloseCommand.name[1]: CloseCommand,
    HelloCommand.name: HelloCommand,
    AddAddressCommand.name: AddAddressCommand,
    ChangeAddressCommand.name: ChangeAddressCommand,
    DeleteAddressCommand.name: DeleteAddressCommand,
    AddBirthdayCommand.name: AddBirthdayCommand,
    ChangeBirthdayCommand.name: ChangeBirthdayCommand,
    DeleteBirthdayCommand.name: DeleteBirthdayCommand,
    GetAllBirthdaysCommand.name: GetAllBirthdaysCommand,
    GetBirthdaysCommand.name: GetBirthdaysCommand,
    AddContactCommand.name: AddContactCommand,
    DeleteContactCommand.name: DeleteContactCommand,
    GetAllContactsCommand.name: GetAllContactsCommand,
    GetContactCommand.name: GetContactCommand,
    AddEmailCommand.name: AddEmailCommand,
    ChangeEmailCommand.name: ChangeEmailCommand,
    DeleteEmailCommand.name: DeleteEmailCommand,
    AddNoteCommand.name: AddNoteCommand,
    ChangeNoteCommand.name: ChangeNoteCommand,
    DeleteNoteCommand.name: DeleteNoteCommand,
    GetAllNotesCommand.name: GetAllNotesCommand,
    GetNoteCommand.name: GetNoteCommand,
    AddPhoneCommand.name: AddPhoneCommand,
    ChangePhoneCommand.name: ChangePhoneCommand,
    DeletePhoneCommand.name: DeletePhoneCommand,
    AddTagCommand.name: AddTagCommand,
    ChangeTagCommand.name: ChangeTagCommand,
    DeleteTagCommand.name: DeleteTagCommand,
    GetTagCommand.name: GetTagCommand,
    SortByTagsCommand.name: SortByTagsCommand,
    HelpCommand.name: HelpCommand
}

commands_list = sorted(list(commands.keys()))
command_completer = WordCompleter(commands_list, ignore_case=True)


def parse_input(user_input: str) -> tuple:
    command, *args = user_input.lower().split()
    return command, args


def start():
    contact_book_loaded = Storage.load(ContactBook.pickle_file)
    contact_book: ContactBook = contact_book_loaded if contact_book_loaded else ContactBook()

    notebook_loaded = Storage.load(Notebook.pickle_file)
    notebook: Notebook = notebook_loaded if notebook_loaded else Notebook()

    print(Fore.YELLOW + "Welcome to the assistant bot!")

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print(Fore.RED + "Input is empty.")
            continue

        if command in commands:
            if hasattr(commands[command], "execute"):
                execute_method = commands[command]().execute
            else:
                execute_method = commands[command]

            unwrapped_function = inspect.unwrap(execute_method)
            sig = inspect.signature(unwrapped_function)

            params = list()
            for param in sig.parameters.values():
                if param.annotation == list:
                    params.append(args)
                elif param.annotation == ContactBook:
                    params.append(contact_book)
                elif param.annotation == Notebook:
                    params.append(notebook)

            response = execute_method(*params)

            if isinstance(response, TableResponse) or isinstance(response, str):
                print(response)
            elif response is False:
                Storage.save(ContactBook.pickle_file, contact_book)
                Storage.save(Notebook.pickle_file, notebook)
                print(Fore.YELLOW + "Good bye!" + Style.RESET_ALL)
                sys.exit(1)
        else:
            print(Fore.RED + "Invalid command.")
