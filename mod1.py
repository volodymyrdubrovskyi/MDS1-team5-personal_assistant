"""
Import necessary modules and classes
"""
from classes import *
from mod2 import nsession
from datetime import datetime
import json

def save_notes_to_file():
    """
    Save the list of notes to a JSON file.

    Args:
        notes (list): List of Note objects to be saved.
    """
    global notes
    with open('notes.json', 'w') as file:
        data = [{'content': note.content, 'tags': note.tags, 'creation_date': note.creation_date.strftime('%Y-%m-%d %H:%M:%S')} for note in notes]
        json.dump(data, file)


# Function to load notes from a JSON file

def load_notes_from_file():
    """
    Load notes from a JSON file and populate the 'notes' list.
    If the file is not found, initialize an empty 'notes' list.
    """
    try:
        with open('notes.json', 'r') as file:
            data = json.load(file)
            for note_data in data:
                content = note_data['content']
                tags = note_data['tags']
                creation_date = datetime.strptime(note_data['creation_date'], '%Y-%m-%d %H:%M:%S')
                note = Note(content, tags)
                note.creation_date = creation_date
                notes.append(note)
    except FileNotFoundError:
        pass


 # Function to add tags to a note and save it

def add_tags_to_note():
    """
    Add a new note with content and tags, and save it to the 'notes' list.
    """
    global notes
    content = nsession.prompt("Enter the content of the note: ")
    tags = nsession.prompt("Enter tags (separated by spaces): ").split()
    note = Note(content, tags)
    notes.append(note)
    save_notes_to_file()  
    

# Function to search notes by a specific tag

def search_notes_by_tag():
    """
    Search for notes based on a specific tag and display the results.
    """
    global notes
    search_tag = nsession.prompt("Enter a tag to search for: ")
    found_notes = [note for note in notes if search_tag in note.tags]
    if found_notes:
        print("Found notes:")
        for i, note in enumerate(found_notes, 1):
            print(f"{i:^3}. Date: {note.creation_date.strftime('%d.%m.%Y %H:%M')}. NOTE: {note.content} (Tags: {', '.join(note.tags)}))")
    else:
        print("No notes found with this tag.")

# Function to sort and display notes by tag

def sort_notes_by_tag():
    """
    Sort and display all existing notes by their tags.
    """
    global notes
    sorted_notes = sorted(notes, key=lambda note: len(note.tags))
    print("All existing notes (Sorted by Tag):")
    for i, note in enumerate(sorted_notes, 1):
        print(f"{i:^3}. Date: {note.creation_date.strftime('%d.%m.%Y %H:%M')}. Number of Tags: [{len(note.tags):^4}]. Note: {note.content}")


# Function to manage notes (add, search, edit, delete, etc.)

def notes_func():
    """
    Main function to manage notes including adding, searching, editing, and deleting notes.
    """
    global notes
    load_notes_from_file()
    while True:
        print("\n1. Add a Note")
        print("2. Search Notes by Tag")
        print("3. Show All Notes (Sorted by Date)")
        print("4. Sort Notes by number of Tags")
        print("5. Edit a Note")
        print("6. Delete a Note")
        print("7. Return to the Main Menu")

        notes_choice = nsession.prompt(">>> Select an option for notes: ")

        if notes_choice == '1':
            add_tags_to_note()  
        elif notes_choice == '2':
            search_notes_by_tag()  
        elif notes_choice == '3':
            if notes:
                sorted_notes = sorted(notes, key=lambda note: note.creation_date)
                print("All existing notes (Sorted by Date):")
                for i, note in enumerate(sorted_notes, 1):
                    print(f"{i:^3}. Date: {note.creation_date.strftime('%d.%m.%Y %H:%M')}. NOTE: {note.content} (Tags: {', '.join(note.tags)}))")
            else:
                print("There are no notes available.")
        elif notes_choice == '4':
            sort_notes_by_tag() 
        elif notes_choice == '5':
            if not notes:
                print("There are no notes to edit.")
            else:
                index_to_edit = int(nsession.prompt("Enter the number of the note you want to edit: ")) - 1
                if 0 <= index_to_edit < len(notes):
                    new_content = nsession.prompt("Enter the new content of the note: ")
                    new_tags = nsession.prompt("Enter new tags (separated by spaces): ").split()
                    notes[index_to_edit].content = new_content
                    notes[index_to_edit].tags = new_tags
                    print("The note has been successfully edited.")
                else:
                    print("Invalid note number.")
        elif notes_choice == '6':
            if not notes:
                print("There are no notes to delete.")
            else:
                index_to_delete = int(nsession.prompt("Enter the number of the note you want to delete: ")) - 1
                if 0 <= index_to_delete < len(notes):
                    del notes[index_to_delete]
                    print("The note has been successfully deleted.")
                else:
                    print("Invalid note number.")
        elif notes_choice == '7':
            break
        else:
            print("Please select an option from 1 to 7. For help, refer to the Help file.")

    save_notes_to_file()

notes=[]