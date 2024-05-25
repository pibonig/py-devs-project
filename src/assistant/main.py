import inspect
import sys

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from lib.storage import Storage
from src.assistant.commands.address.add_address_command import add_address_command
from src.assistant.commands.address.change_address_command import change_address_command
from src.assistant.commands.address.delete_address_command import delete_address_command
from src.assistant.commands.birthday import get_all_birthdays_command, get_birthday_command
from src.assistant.commands.birthday.add_birthday_command import add_birthday_command
from src.assistant.commands.birthday.change_birthday_command import change_birthday_command
from src.assistant.commands.birthday.delete_birthday_command import delete_birthday_command
from src.assistant.commands.close_command import close_command
from src.assistant.commands.contact.add_contact_command import AddContactCommand
from src.assistant.commands.contact.delete_contact_command import delete_contact_command
from src.assistant.commands.contact.get_all_contacts_command import get_all_contacts_command
from src.assistant.commands.contact.get_contact_command import get_contact_command
from src.assistant.commands.email.add_email_command import add_email_command
from src.assistant.commands.email.change_email_command import change_email_command
from src.assistant.commands.email.delete_email_command import delete_email_command
from src.assistant.commands.hello_command import hello_command
from src.assistant.commands.help.help_command import help_command
from src.assistant.commands.note.add_note_command import AddNoteCommand
from src.assistant.commands.note.add_tag_command import AddTagCommand
from src.assistant.commands.note.change_note_command import ChangeNoteCommand
from src.assistant.commands.note.delete_note_command import DeleteNoteCommand
from src.assistant.commands.note.delete_tag_command import DeleteTagCommand
from src.assistant.commands.note.get_all_notes_command import GetAllNotesCommand
from src.assistant.commands.note.get_note_command import GetNoteCommand
from src.assistant.commands.note.get_tag_command import GetTagCommand
from src.assistant.commands.note.sort_by_tags_command import SortByTagsCommand
from src.assistant.commands.phone.add_phone_command import add_phone_command
from src.assistant.commands.phone.change_phone_command import change_phone_command
from src.assistant.commands.phone.delete_phone_command import delete_phone_command
from src.models.contact_book.contact_book import ContactBook
from src.models.notebook.notebook import Notebook
from src.response.table_response import TableResponse

commands = {
    "close": close_command,
    "exit": close_command,
    "hello": hello_command,
    "add_address": add_address_command,
    "change_address": change_address_command,
    "delete_address": delete_address_command,
    "add_birthday": add_birthday_command,
    "change_birthday": change_birthday_command,
    "delete_birthday": delete_birthday_command,
    "get_all_birthdays": get_all_birthdays_command,
    "get_birthday": get_birthday_command,
    AddContactCommand.name: AddContactCommand,
    "delete_contact": delete_contact_command,
    "get_all_contacts": get_all_contacts_command,
    "get_contact": get_contact_command,
    "add_email": add_email_command,
    "change_email": change_email_command,
    "delete_email": delete_email_command,
    AddNoteCommand.name: AddNoteCommand,
    ChangeNoteCommand.name: ChangeNoteCommand,
    DeleteNoteCommand.name: DeleteNoteCommand,
    GetAllNotesCommand.name: GetAllNotesCommand,
    GetNoteCommand.name: GetNoteCommand,
    "add_phone": add_phone_command,
    "change_phone": change_phone_command,
    "delete_phone": delete_phone_command,
    AddTagCommand.name: AddTagCommand,
    DeleteTagCommand.name: DeleteTagCommand,
    GetTagCommand.name: GetTagCommand,
    SortByTagsCommand.name: SortByTagsCommand,
    "help": help_command
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

    print("Welcome to the assistant bot!")

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Input is empty.")
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
                print("Good bye!")
                sys.exit(1)
        else:
            print("Invalid command.")
