import datetime
from data.classes import AddressBook, Birthday, DateFormatError, TypeEmailError, RecordNotFindError, PhoneNotFindError, Record, LenPhoneError, TypePhoneError

def upcoming_birthdays(book, args):
    """
    Returns a list of contacts from the contact book whose birthdays are approaching.

    :param book: The contact book object where contact data is stored.

    :param args: Function arguments. args[0] specifies the number of days to consider for upcoming birthdays.

    :return: A list of contacts whose birthdays are approaching and meet the criteria.

    The function checks all contacts in the book and determines if each contact's birthday is approaching within the
    specified number of days, which is passed as the first element in `args`. If a contact's birthday is approaching,
    it is added to the `birthday_contacts` list. Contacts whose birthdays have already passed or are yet to come are
    not included in the result.

    For example, if `args[0]` is set to 7, the function will return a list of contacts whose birthdays are approaching
    within the next 7 days.
    """
    today = datetime.date.today()
    birthday_contacts = []
    this_year = today.year
    try:
        for _, record in book.data.items():
            if record.birthday is not None:
                days_until_birthday = (record.birthday.value.replace(year=this_year) - today).days
                if days_until_birthday < 0:
                    days_until_birthday = (record.birthday.value.replace(year=this_year + 1) - today).days
                if 0 <= days_until_birthday <= int(args[0]):
                    birthday_contacts.append(record)

        if birthday_contacts:
            return birthday_contacts
        else:
            print('There are no upcoming birthdays')
            return False
    except IndexError:
        print('Command should be followed by "number of days" parameter')
    except ValueError:
        print('"number of days" parameter should be integer')

def birthday_record(book:AddressBook, args:list):
    """
    Add birthday for record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        birthday (Birthday): user birthday 
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.birthday = Birthday(args[1])
                print('Birthday added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except DateFormatError:
            print('Error: Date format must be: DD.MM.YYYY')
    else:
        print('Error: Invalid command format.')

def del_birthday(book:AddressBook, args:list):
    """
    Delete birthday from record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.birthday = None
            print('Birthday deleted sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')


def address_record(book:AddressBook, args:list):
    """
    Add address for record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        address (str): user address 
    """
    if len(args) >=2:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.address = ' '.join(s for s in args[1:])
            print('Address added sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command.')

def del_address(book:AddressBook, args:list):
    """
    Delete address from record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            rec = book.data[int(args[0])]
            rec.address = ''
            print('Address deleted sucessfully.')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command.')

def add_email_in_rec(book:AddressBook, args:list):
    """
    Add email for record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        email (Email): user email 
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.add_email(args[1])
                print('Email added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except TypeEmailError:
            print('Error: Wrong email format')
    else:
        print('Error: Invalid command format.')

def edit_email_in_rec(book:AddressBook, args:list):
    """
    Edit email for record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        email (Email): user email 
    """
    if len(args) ==3:
        try:
            rec = book.data[int(args[0])]
            rec.edit_email(args[1], args[2])
            print('Email changed sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Email to change is not found.')
        except TypeEmailError:
            print('Error: Wrong email format')    
    else:
        print('Error: Invalid command format.')

def del_email_in_rec(book:AddressBook, args:list):
    """
    Delete email for record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        email (Email): user email 
    """
    if len(args) ==2:
        try:
            rec = book.data[int(args[0])]
            rec.remove_email(args[1])
            print('Email deleted sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Email to delete is not found.')
    else:
        print('Error: Invalid command format.')

def add_record(book:AddressBook, args:list):
    """
    Adding new record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        name (Name): user name 
    """
    if len(args) ==1:
        book.add_record(Record(args[0], book))
        print('Record created sucessfully')
    else:
        print('Error: Invalid command format.')

def edit_record(book:AddressBook, args:list):
    """
    Edit Name in the record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        name (Name): new user name 
    """
    if len(args) ==2:
        if int(args[0]) in book.data:
            book.edit_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def del_record(book:AddressBook, args:list):
    """
    Delete the record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
    """
    if len(args) ==1:
        if int(args[0]) in book.data:
            book.del_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

def add_phone_in_rec(book:AddressBook, args:list):
    """
    Add phone to the record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        phone (str): phone number to add
    """
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.add_phone(args[1])
                print('Phone added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except LenPhoneError:
            print('Error: Phone must be 10 symbols')
        except TypePhoneError:
            print('Error: Phone must be 10 symbols')
    else:
        print('Error: Invalid command format.')

def edit_phone_in_rec(book:AddressBook, args:list):
    """
    Replace old phone by the new one in the record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        old phone (str): phone number to change
        new phone (str): new phone number
    """
    if len(args) ==3:
        try:
            rec = book.data[int(args[0])]
            rec.edit_phone(args[1], args[2])
            print('Phone changed sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except LenPhoneError:
            print('Error: Phone must be 10 symbols')
        except PhoneNotFindError:
            print('Error: Phone to change is not found.')
        except TypePhoneError:
            print('Error: Phone must consist from digits')
    else:
        print('Error: Invalid command format.')

def del_phone_in_rec(book:AddressBook, args:list):
    """
    Delete phone in the record in Adress Book
    Args:
        book (AddressBook): An AddressBook instance containing contact information.
        user id (int): User ID in adress book
        phone (str): phone number to delete
    """
    if len(args) ==2:
        try:
            rec = book.data[int(args[0])]
            rec.remove_phone(args[1])
            print('Phone deleted sucessfully.')
        except RecordNotFindError:
            print('Error: User not found.')
        except PhoneNotFindError:
            print('Error: Phone to delete is not found.')
    else:
        print('Error: Invalid command format.')

def find_in_records(book:AddressBook, args:list):
    """
    search in Adress Book
    Args:
        search string (str): string for search in address book fields: Name, Adress, Phones, Emails, Birthday
    """
    if len(args) ==1 and len(args[0]) > 1:
        count = 0
        sstring = args[0].lower()
        for _, record in book.data.items():
            if record.searchstring().find(sstring) >=0:
                print(record)
                count += 1
        print(f'Search complete. Total {count} records found.')    
    else:
        print('Error: Invalid command format. Search string must be more then 2 symbols')