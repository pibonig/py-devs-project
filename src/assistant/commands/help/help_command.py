from src.response.base_response import BaseResponse
from src.response.table_response import TableResponse


def help_command() -> BaseResponse:
    commands_info = [
        ['Command', 'Parameters', 'Description'],
        ['close, exit', '', 'Exit the bot'],
        ['hello', '', 'Say hello'],
        ['add_address', '[Name] [Address]', 'Add address to contact'],
        ['change_address', '[Name] [Address]', 'Change contact address'],
        ['delete_address', '[Name] [Address]', 'Delete contact address'],
        ['add_birthday', '[Name] [Birthday]', 'Add birthday to contact'],
        ['change_birthday', '[Name] [Birthday]', 'Change contact birthday'],
        ['delete_birthday', '[Name] [Birthday]', 'Delete contact birthday'],
        ['get_all_birthdays', '', 'Get all birthdays'],
        ['get_birthday', '[Name] [Birthday]', 'Get contact birthday'],
        ['add_contact', '[Name]', 'Add a new contact'],
        ['delete_contact', '[Name]', 'Delete a contact'],
        ['get_all_contacts', '', 'Get all contacts'],
        ['get_contact', '[Name]', 'Get contact details'],
        ['add_email', '[Name] [Email]', 'Add email to contact'],
        ['change_email', '[Name] [Email]', 'Change contact email'],
        ['delete_email', '[Name] [Email]', 'Delete contact email'],
        ['add_note', '[Note_title] [Note]', 'Add note to contact'],
        ['change_note', '[Note_title] [Note]', 'Change contact note'],
        ['delete_note', '[Note_title]', 'Delete contact note'],
        ['get_all_notes', '', 'Get all notes'],
        ['get_note', '[Note_title]', 'Get contact note'],
        ['add_phone', '[Name] [Phone]', 'Add phone to contact'],
        ['change_phone', '[Name] [Phone]', 'Change contact phone'],
        ['delete_phone', '[Name] [Phone]', 'Delete contact phone'],
        ['add_tag', '[Note_title] [Tag]', 'Add tag to note'],
        ['delete_tag', '[Note_title] [Tag]', 'Delete tag from note'],
        ['get_tag', '[Tag]', 'Get note tags'],
        ['sort_by_tags', '[Tag]', 'Sort notes by tags']
    ]

    headers = commands_info[0]
    body = commands_info[1:]
    return TableResponse(headers, body)
