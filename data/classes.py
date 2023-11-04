from collections import UserDict
import re
import datetime
import pickle


# to handle of phone number not equal Phone.MAX_PHONE_LEN length
class LenPhoneError(Exception):
    pass

# to handle if phone conteains non-digits symbols
class TypePhoneError(Exception):
    pass

# to handle if phone doesn't found in record
class PhoneNotFindError(Exception):
    pass

# to handle if record doesn't found in adress book
class RecordNotFindError(Exception):
    pass

# to handle wrong data input format
class DateFormatError(Exception):
    pass

class TypeEmailError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Birthday(Field):
    def __init__(self, date=None):
            result = re.findall(r'\d\d.\d\d.\d\d\d\d', date)
            if result != []:
                self.value = datetime.date(year=int(date[6:10]), month=int(date[3:5]), day=int(date[0:2]))
            else:
                raise DateFormatError

    def __str__(self) -> str:
        return 'No Data' if self.value == None else self.value.strftime('%d.%m.%Y')
    
class Phone(Field):
    MAX_PHONE_LEN = 10

    def __init__(self, value):
        self.value = value

class Email(Field):
    def __init__(self, value):
        self.value = value

class Record:
    def __init__(self, name, book, birthday=None):
        self.user_id = book.user_id_counter
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = birthday
        self.address = ''

    # to add an email to record
    def add_email(self, email):
        filteredemail = re.findall(r"[A-Za-z,0-9]{1}[a-z,A-Z,.,_,0-9]{0,}@[a-zA-Z]+[.]{1}[a-z,A-Z,.]{2,}", email)
        if len(filteredemail) > 0 and email[-1] not in ['.',',','/','\\']:
            new_email = True
            for e in self.emails:
                if e.value == filteredemail[0]:
                    new_email = False
            if new_email:
                self.emails.append(Email(filteredemail[0]))
                return True
        else:
            raise TypeEmailError

    # to remove an email from record
    def remove_email(self, email):
        find_email = False
        for e in self.emails:
            if e.value == email:
                find_email = True
                email_to_remove = e
        if find_email:
            self.emails.remove(email_to_remove)
        else:
            raise PhoneNotFindError

    # to edit email in record
    def edit_email(self, email_old, email_new):
        find_email = False
        for e in self.emails:
            if e.value == email_old:
                find_email = True
                email_to_remove = e
        if find_email:
            if self.add_email(email_new):
                self.emails.remove(email_to_remove)
        else:
            raise PhoneNotFindError


    # to add phone to record
    def add_phone(self, phone):
        if len(phone) != Phone.MAX_PHONE_LEN:
            raise LenPhoneError
        elif not phone.isdigit():
            raise TypePhoneError
        else:
            new_phone = True
            for p in self.phones:
                if p.value == phone:
                    new_phone = False
            if new_phone:
                self.phones.append(Phone(phone))
        
    # to remove phone from record
    def remove_phone(self, phone):
        find_phone = False
        for p in self.phones:
            if p.value == phone:
                find_phone = True
                phone_to_remove = p
        if find_phone:
            self.phones.remove(phone_to_remove)
        else:
            raise PhoneNotFindError

    # to change one phone to another
    def edit_phone(self, phone_old, phone_new):
        if len(phone_new) != Phone.MAX_PHONE_LEN:
            raise LenPhoneError
        elif not phone_new.isdigit():
            raise TypePhoneError
        else:
            sucsess = False
            for phone in self.phones:
                if phone.value == phone_old:
                    phone.value = phone_new
                    sucsess = True
            if not sucsess:
                raise PhoneNotFindError

    # to create s string to use this string for search
    def searchstring(self):
        phones_line = f"{' '.join(p.value for p in self.phones)}" if self.phones else ""
        birthday_line = f"{self.birthday.__str__()}" if self.birthday else ""
        emails_line = f"{' '.join(p.value for p in self.emails)}" if self.emails else ""
        address_line = f"{self.address}" if self.address else ""
        res = f"{self.user_id} {self.name.value} " + phones_line + birthday_line + emails_line + address_line
        return res.lower()

    def __str__(self):
        phones_line = f"; phones: {', '.join(p.value for p in self.phones)}" if self.phones else ""
        birthday_line = f"; birthday: {self.birthday.__str__()}" if self.birthday else ""
        emails_line = f"; emails: {', '.join(p.value for p in self.emails)}" if self.emails else ""
        address_line = f"; adress: {self.address}" if self.address else ""
        res = f"Contact id: {self.user_id}, name: {self.name.value}" + phones_line + birthday_line + emails_line + address_line
        return res
    
class AddressBook(UserDict):
    def __init__(self):
        """
        Initialize an AddressBook with a user ID counter and a data dictionary.
        """
        self.user_id_counter = 0
        self.data = UserDict()

    # to load adress book from file
    def read_from_file(self):
        """
        Read data from a file and return an AddressBook instance.
        """
        with open('data\\abook.dat', 'rb') as fh:
            return pickle.load(fh)

    # to save adress book to file
    def save_to_file(self):
        """
        Save the AddressBook instance to a file.
        """
        with open('data\\abook.dat', 'wb') as fh:
            pickle.dump(self, fh)
    
    def add_record(self, record):
        """
        Add a new record to the AddressBook.

        Args:
            record: The record to add to the AddressBook.
        """
        self.data[self.user_id_counter] = record
        self.user_id_counter += 1
    
    def edit_record(self, args):
        """
        Edit the name of a record in the AddressBook.
        Args:
            args (list): A list containing the record ID and the new name.
        """
        self.data[int(args[0])].name.value = args[1]

    def del_record(self, args):
        """
        Delete a record from the AddressBook.

        Args:
            args (list): A list containing the record ID to be deleted.
        """
        self.data.pop(int(args[0]))

# class with user notes
class Note:
    def __init__(self, nbook, content):
        """
        Initialize a Note object with content, tags, and creation date.

        Args:
            content (str): The content of the note.
            tags (list): A list of tags associated with the note.
        """
        self.note_id = nbook.note_id_counter
        self.content = content
        self.tags = list()
        self.creation_date = datetime.datetime.now()
    
    def add_tag(self, tag):
        new_tag = True
        for t in self.tags:
            if t == tag:
                new_tag = False
        if new_tag:
            self.tags.append(tag)
    
    # to remove tag from record
    def remove_tag(self, tag):
        find_tag = False
        for t in self.tags:
            if t == tag:
                find_tag = True
        if find_tag:
            self.tags.remove(tag)
        else:
            raise PhoneNotFindError

    def searchstring(self):
        tags_line = f"{' '.join(p for p in self.tags)}" if self.tags else ""
        res = f"{self.content} " + tags_line
        return res.lower()
    
    def search_tag(self):
        res = f"{' '.join(p for p in self.tags)}" if self.tags else ""
        return res.lower()

    def __str__(self):
        #return f"ID: {self.note_id:^3}. DATE: {self.creation_date.strftime('%d.%m.%Y %H:%M')}. NOTE: {self.content} [Tags: {', '.join(self.tags)}]"
        return f"ID: {self.note_id:^3}| Tags: {', '.join(self.tags):>20} | {self.content:<70}"

# NoteBook class
class NoteBook(UserDict):
    def __init__(self):
        """
        Initialize an NoteBook with a user ID counter and a data dictionary.
        """
        self.note_id_counter = 0
        self.data = UserDict()
        self.max_tags_len = 5 + 2

    def add_record(self,note):
        """
        Add a new note to the NoteBook.
        Args:
            note: The record to add to the NoteBook.
        """
        self.data[self.note_id_counter] = note
        self.note_id_counter += 1

    def read_from_file(self):
        """
        Read data from a file and return an AddressBook instance.
        """
        with open('data\\nbook.dat', 'rb') as fh:
            return pickle.load(fh)
        
    def save_to_file(self):
        """
        Save the NoteBook instance to a file.
        """
        with open('data\\nbook.dat', 'wb') as fh:
            pickle.dump(self, fh)

    def edit_record(self, args):
        """
        Edit the name of a record in the AddressBook.
        Args:
            args (list): A list containing the record ID and the new name.
        """
        self.data[int(args[0])].content = (' '.join(args[1:]))

    def del_note(self, args):
        """
        Delete a Note from the Note Book.
        Args:
            args (list): A list containing the record ID to be deleted.
        """
        self.data.pop(int(args[0]))