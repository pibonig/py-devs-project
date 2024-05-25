**Table of Contents**

- [Installation](#installation)
- [Bot commands](#bot-commands)

## Installation

Create virtual environment

```bash
python -m venv .venv

# or

python3 -m venv .venv
```

Activate virtual environment

```bash
# На Windows у командному рядку (CMD):
.\.venv\Scripts\activate.bat

# На Windows у PowerShell:
.\.venv\Scripts\Activate.ps1

# На macOS та Linux:
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

## Bot commands

| Command           | Parameters                        | Description                                              |
|-------------------|-----------------------------------|----------------------------------------------------------|
| close             |                                   | Exit the bot                                             |
| exit              |                                   | Exit the bot                                             |
| hello             |                                   | Say hello                                                |
| add_address       | \<name> \<address>                | Add address to contact                                   |
| change_address    | \<name> \<address>                | Change contact address                                   |
| delete_address    | \<name> \<address>                | Delete contact address                                   |
| add_birthday      | \<name> \<date>                   | Add a birthday to a contact                              |
| change_birthday   | \<name> \<date>                   | Change the birthday of a contact                         |
| delete_birthday   | \<name>                           | Delete the birthday of a contact                         |
| get_all_birthdays |                                   | Show all contacts with their birthdays                   |
| get_birthdays     | \<days>                           | Get upcoming birthdays within a specified number of days |
| add_contact       | \<name> \<phone>                  | Add a new contact                                        |
| delete_contact    | \<name>                           | Delete the contact                                       |
| get_all_contacts  |                                   | Get all contacts                                         |
| get_contact       | \<name>                           | Get contact details                                      |
| add_email         | \<name> \<email>                  | Add email to contact                                     |
| change_email      | \<name> \<email>                  | Change contact email                                     |
| delete_email      | \<name>                           | Delete contact email                                     |
| add_note          | \<title> \<content>               | Add a new note                                           |
| change_note       | \<note_title> \<content>          | Change the content of an existing note                   |
| delete_note       | \<note_title>                     | Delete an existing note by title                         |
| get_all_notes     |                                   | Get all notes                                            |
| get_note          | \<title>                          | Retrieve a note by its title                             |
| add_phone         | \<name> \<phone>                  | Add phone to contact                                     |
| change_phone      | \<name> \<old_phone> \<new_phone> | Change contact phone                                     |
| delete_phone      | \<name> \<phone>                  | Delete contact phone                                     |
| add_tag           | \<note_title> \<tag>              | Add tag to note                                          |
| delete_tag        | \<note_title> \<tag>              | Delete a tag from an existing note                       |
| get_tag           | \<tag>                            | Retrieve notes with a specific tag                       |
| sort_by_tags      | \<tag>                            | Sort notes by a specific tag                             |
