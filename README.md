 # Personal Assistant

This is a Python application that provides functionality to manage an address book and take notes. The application allows you to create, edit, and delete contact records, add and remove phone numbers and email addresses, manage birthdays and addresses, and search for records based on various criteria. Additionally, you can create and manage notes, search for notes by tags, and view all notes sorted by date.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command Line Interface](#command-line-interface)
- [Commands](#commands)
- [License](#license)

## Features

### Address Book Management

- Create and manage contact records with the following information:
  - Name
  - Phone numbers
  - Email addresses
  - Birthday
  - Address
- Edit and delete contact records.
- Add, edit, or delete phone numbers and email addresses for a contact.
- Set or remove a birthday for a contact.
- Set or remove an address for a contact.
- Search for contact records based on a search string.
- List upcoming birthdays within a specified number of days.
- View all contact records.

### Notes Management

- Create and manage notes with content and tags.
- Search for notes by tags.
- View all notes sorted by date.
- Edit or delete notes.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/volodymyrdubrovskyi/project-secutor5.git
   ```
2. Install the required dependencies:

    ```
    pip install prompt_toolkit
    ```
## Usage

1. Run the application by executing the main.py file:

    ```
    python main.py
    ```
2. Follow the on-screen prompts to use the application.

## Command Line Interface
This application utilizes the prompt_toolkit library to provide a command line interface for interacting with the program. The prompt_toolkit package provides features such as auto-completion and history tracking.

To use the command line interface effectively, you can take advantage of the following features:

Auto-Completion: As you type commands, the application will provide auto-completion suggestions for available commands. For example, if you start typing "ad" and press the Tab key, the application will suggest commands like "add," "add-phone," and more.

History Tracking: Your command history is tracked, so you can use the up and down arrow keys to navigate through your previous commands.

## Commands
The application supports the following commands:

- add [Name]: Create a new contact record with the specified name.
- edit [Contact_id] [new_Name]: Edit the name of a contact record.
- del [Contact_id]: Remove a contact record.
- add-phone [Contact_id] [Phone]: Add a phone number to a contact.
- edit-phone [Contact_id] [Phone] [new_Phone]: Replace a phone number in a contact.
- del-phone [Contact_id] [Phone]: Remove a phone number from a contact.
- add-email [Contact_id] [Email]: Add an email address to a contact.
- edit-email [Contact_id] [Email] [new_Email]: Replace an email address in a contact.
- del-email [Contact_id] [Email]: Remove an email address from a contact.
- birthday [Contact_id] [Birthday]: Set a birthday for a contact.
- del-birthday [Contact_id]: Remove a birthday from a contact.
- address [Contact_id] [Address]: Set an address for a contact.
- del-address [Contact_id]: Remove an address from a contact.
- find [searchstring]: Search for contact records based on a search string.
- help: Display a list of available commands.
- note: Add a note to Note Book.
- all-notes: List all notes
- edit-note [Note_id] [Note]: Edit text of note
- del-note [Note_id]: Remove note from Note Book
- add-tag [Note_id] [Tag]: Add tag to note
- del-tag [Note_id] [Tag]: Remove tag from note
- find-notes [searchstring]: List all notes with search string data in note and tags. Search string must be 2 symbols minimum
- find-tags [searchstring]: List all notes with search string data in tags. Searchstring must be 2 symbols minimum
- sort-tag: List all notes sorted by number of tags
- next-birthdays [int]: Show upcoming birthdays within the specified number of days.
- all: List all contact records.
- close or exit: Exit the application.

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) for details.