from data.classes import NoteBook, Note, PhoneNotFindError

def add_note(nbook: NoteBook, args:list):
    """
    Create a new record in Note Book
    Args:
        nbook (NoteBook): NoteBook instance containing contact information.
        Note (str): Note 
    """
    if len(args) >=1:
        nbook.add_record(Note(nbook, (' '.join(args))))
        print('Note created sucessfully')
    else:
        print('Error: Invalid command format.')

def edit_note(nbook: NoteBook, args:list):
    """
    Edit Note in the Note Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        note id (int): Note ID in Note Book
        Note (Name): new Note text 
    """
    if len(args) >=2:
        if int(args[0]) in nbook.data:
            nbook.edit_record(args)
            print('Record sucessfully edited')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_note(nbook: NoteBook, args:list):
    """
    Delete the note in Notes Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        note id (int): Note ID in Note Book
    """
    if len(args) ==1:
        if int(args[0]) in nbook.data:
            nbook.del_note(args)
            print('Note sucessfully deleted')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def add_tag(nbook: NoteBook, args:list):
    """
    Add tag for note_id Note in Notes Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        note id (int): Note ID in Note Book
        tag (str): tag for Note
    """
    if len(args) ==2:
        if int(args[0]) in nbook.data:
            rec = nbook.data[int(args[0])]
            rec.add_tag(args[1])
            print('Tag added sucessfully.')
        else:
            print(f'Note id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_tag(nbook: NoteBook, args:list):
    """
    Removes tag for note_id Note in Notes Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        note id (int): Note ID in Note Book
        tag (str): tag for removing
    """
    if len(args) ==2:
        try:
            rec = nbook.data[int(args[0])]
            rec.remove_tag(args[1])
            print('Tag deleted sucessfully.')
        except KeyError:
            print(f'Note id {args[0]} not found')
        except PhoneNotFindError:
            print('Error: Tag to delete is not found.')
    else:
        print('Error: Invalid command format.')

def find_in_notes(nbook: NoteBook, args:list):
    """
    search Notes and tags in Notes Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        serchstring (str): serch string. Must be 2 symbols minimum
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in nbook.data.items():
            if record.searchstring().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')

def find_in_tags(nbook: NoteBook, args:list):
    """
    search tags in Notes Book
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
        serchstring (str): serch string. Must be 2 symbols minimum
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in nbook.data.items():
            if record.search_tag().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')

def sort_by_tags(nbook: NoteBook, args:list):
    """
    list all Notes sorted by number of tags
    Args:
        nbook (NoteBook): An NoteBook instance containing contact information.
    """
    if len(args) == 0:
        #print(nbook.data.values)
        notes = []
        for _, n in nbook.data.items():
            notes.append(n)
        sorted_notes = sorted(notes, key=lambda note: len(note.tags))
        print("All existing notes (Sorted by Tag):")
        for i, note in enumerate(sorted_notes, 1):
            print(f"ID: {note.note_id:^3}| Number of Tags: [{len(note.tags):^4}]| NOTE: {note.content}")
    else:
        print('Error: Invalid command format.')
