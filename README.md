 # Personal Assistant

This is a Python application that provides functionality to manage an address book and take notes. The application allows you to create, edit, and delete contact records, add and remove phone numbers and email addresses, manage birthdays and addresses, and search for records based on various criteria. Additionally, you can create and manage notes, search for notes by tags, and view all notes sorted by date.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
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
- note: Switch to the notes management interface.
- next-birthdays [int]: Show upcoming birthdays within the specified number of days.
- all: List all contact records.
- close or exit: Exit the application.

## License
This project is licensed under the MIT License. See the [LICENSE](#https://opensource.org/license/mit/) for details.