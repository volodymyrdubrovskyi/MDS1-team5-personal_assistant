from classes import *
from mod1 import *
from mod2 import nsession
import json

def save_notes_to_file(notes):
    with open('notes.json', 'w') as file:
        data = [{'content': note.content, 'tags': note.tags, 'creation_date': note.creation_date.strftime('%Y-%m-%d %H:%M:%S')} for note in notes]
        json.dump(data, file)

def load_notes_from_file():
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
        notes = []

  
def notes_func(notes):
    load_notes_from_file() 
    while True:
        print("\n1. Add a Note")
        print("2. Search Notes by Tag")
        print("3. Show All Notes (Sorted by Date)")
        print("4. Edit a Note")
        print("5. Delete a Note")
        print("6. Return to the Main Menu")
        
        notes_choice = nsession.prompt("Select an option for notes: ")

        if notes_choice == '1':
            
            content = nsession.prompt("Enter the content of the note: ")
            tags = nsession.prompt("Enter tags (separated by spaces): ").split()
            note = Note(content, tags)  
            notes.append(note)  
            save_notes_to_file()  

        elif notes_choice == '2':
          
            search_tag = nsession.prompt("Enter a tag to search for: ")
            found_notes = [note for note in notes if search_tag in note.tags]
            if found_notes:
                print("Found notes:")
                for i, note in enumerate(found_notes, 1):
                    print(f"{i}. {note.content} (Tags: {', '.join(note.tags)}) (Date: {note.creation_date})")
            else:
                print("No notes found with this tag.")

        elif notes_choice == '3':
            
            if notes:
                sorted_notes = sorted(notes, key=lambda note: note.creation_date)
                print("All existing notes (Sorted by Date):")
                for i, note in enumerate(sorted_notes, 1):
                    print(f"{i}. {note.content} (Tags: {', '.join(note.tags)}) (Date: {note.creation_date})")
            else:
                print("There are no notes available.")

        elif notes_choice == '4':
            
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

        elif notes_choice == '5':
           
            if not notes:
                print("There are no notes to delete.")
            else:
                index_to_delete = int(nsession.prompt("Enter the number of the note you want to delete: ")) - 1
                if 0 <= index_to_delete < len(notes):
                    del notes[index_to_delete]
                    print("The note has been successfully deleted.")
                else:
                    print("Invalid note number.")

        elif notes_choice == '6':
            break


        else:
            print("Please select an option from 1 to 6. For help, refer to the Help file.")


    save_notes_to_file(notes)

