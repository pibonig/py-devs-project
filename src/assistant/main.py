import inspect

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from src.assistant.commands.address.add_address_command import add_address_command
from src.assistant.commands.address.change_address_command import change_address_command
from src.assistant.commands.address.delete_address_command import delete_address_command
from src.assistant.commands.birthday import get_all_birthdays_command, get_birthday_command
from src.assistant.commands.birthday.add_birthday_command import add_birthday_command
from src.assistant.commands.birthday.change_birthday_command import change_birthday_command
from src.assistant.commands.birthday.delete_birthday_command import delete_birthday_command
from src.assistant.commands.close_command import close_command
from src.assistant.commands.contact.add_contact_command import add_contact_command
from src.assistant.commands.contact.delete_contact_command import delete_contact_command
from src.assistant.commands.contact.get_all_contacts_command import get_all_contacts_command
from src.assistant.commands.contact.get_contact_command import get_contact_command
from src.assistant.commands.email.add_email_command import add_email_command
from src.assistant.commands.email.change_email_command import change_email_command
from src.assistant.commands.email.delete_email_command import delete_email_command
from src.assistant.commands.hello_command import hello_command
from src.assistant.commands.help.help_command import help_command
from src.assistant.commands.note.add_note_command import add_note_command
from src.assistant.commands.note.add_tag_command import add_tag_command
from src.assistant.commands.note.change_note_command import change_note_command
from src.assistant.commands.note.delete_note_command import delete_note_command
from src.assistant.commands.note.delete_tag_command import delete_tag_command
from src.assistant.commands.note.get_all_notes_command import get_all_notes_command
from src.assistant.commands.note.get_note_command import get_note_command
from src.assistant.commands.note.get_tag_command import get_tag_command
from src.assistant.commands.note.sort_by_tags_command import sort_by_tags
from src.assistant.commands.phone.add_phone_command import add_phone_command
from src.assistant.commands.phone.change_phone_command import change_phone_command
from src.assistant.commands.phone.delete_phone_command import delete_phone_command
from src.models.contact_book.contact_book import ContactBook
from src.response.base_response import BaseResponse

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
    "add_contact": add_contact_command,
    "delete_contact": delete_contact_command,
    "get_all_contacts": get_all_contacts_command,
    "get_contact": get_contact_command,
    "add_email": add_email_command,
    "change_email": change_email_command,
    "delete_email": delete_email_command,
    "add_note": add_note_command,
    "change_note": change_note_command,
    "delete_note": delete_note_command,
    "get_all_notes": get_all_notes_command,
    "get_note": get_note_command,
    "add_phone": add_phone_command,
    "change_phone": change_phone_command,
    "delete_phone": delete_phone_command,
    "add_tag": add_tag_command,
    "delete_tag": delete_tag_command,
    "get_tag": get_tag_command,
    "sort_by_tags": sort_by_tags,
    "help": help_command
}

commands_list = list(commands.keys())

command_completer = WordCompleter(commands_list, ignore_case=True)


def parse_input(user_input: str) -> tuple:
    command, *args = user_input.lower().split()
    return command, args


def start():
    # TODO: load book from storage
    contact_book = ContactBook()

    print("Welcome to the assistant bot!")

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Input is empty.")
            continue

        if command in commands:
            unwrapped_function = inspect.unwrap(commands[command])
            sig = inspect.signature(unwrapped_function)
            response = None

            if len(sig.parameters) == 0:
                response = commands[command]()
            elif len(sig.parameters) == 1:
                response = commands[command](contact_book)
            elif len(sig.parameters) == 2:
                response = commands[command](args, contact_book)

            if isinstance(response, BaseResponse):
                print(response)
        else:
            print("Invalid command.")
