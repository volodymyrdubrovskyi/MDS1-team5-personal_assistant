from classes import *
from mod1 import *
def notes_func():
    while True:
        print("1. Add a Note")
        print("2. Search Notes by Tag")
        print("3. Show All Notes (Sorted by Date)")
        print("4. Edit a Note")
        print("5. Delete a Note")
        print("6. Return to the Main Menu")

        notes_choice = input("Select an option for notes: ")

        if notes_choice == '1':
            # Add a new note
            content = input("Enter the content of the note: ")
            tags = input("Enter tags (separated by spaces): ").split()
            note = Note(content, tags)  # Create a Note object
            notes.append(note)  # Add the note to the list

        elif notes_choice == '2':
            # Search notes by tag
            search_tag = input("Enter a tag to search for: ")
            found_notes = [note for note in notes if search_tag in note.tags]
            if found_notes:
                print("Found notes:")
                for i, note in enumerate(found_notes, 1):
                    print(f"{i}. {note.content} (Tags: {', '.join(note.tags)}) (Date: {note.creation_date})")
            else:
                print("No notes found with this tag.")

        elif notes_choice == '3':
            # Show all existing notes sorted by date
            if notes:
                sorted_notes = sorted(notes, key=lambda note: note.creation_date)
                print("All existing notes (Sorted by Date):")
                for i, note in enumerate(sorted_notes, 1):
                    print(f"{i}. {note.content} (Tags: {', '.join(note.tags)}) (Date: {note.creation_date})")
            else:
                print("There are no notes available.")

        elif notes_choice == '4':
            # Edit a selected note
            if not notes:
                print("There are no notes to edit.")
            else:
                index_to_edit = int(input("Enter the number of the note you want to edit: ")) - 1
                if 0 <= index_to edit < len(notes):
                    new_content = input("Enter the new content of the note: ")
                    new_tags = input("Enter new tags (separated by spaces): ").split()
                    notes[index_to_edit].content = new_content
                    notes[index_to_edit].tags = new_tags
                    print("The note has been successfully edited.")
                else:
                    print("Invalid note number.")

        elif notes_choice == '5':
            # Delete a selected note
            if not notes:
                print("There are no notes to delete.")
            else:
                index_to_delete = int(input("Enter the number of the note you want to delete: ")) - 1
                if 0 <= index_to_delete < len(notes):
                    del notes[index_to_delete]
                    print("The note has been successfully deleted.")
                else:
                    print("Invalid note number.")

        elif notes_choice == '6':
            break

if __name__ == "__main__":
    while True:
        print("1. Notes Menu")
        print("2. Another Option (add your own options)")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            notes_func()
        elif choice == '2':
            # Implement your other options here
            pass
        elif choice == '3':
            print("Goodbye!")
            break
