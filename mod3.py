from classes import *

def birthday_record(book:AddressBook, args:list):
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

# 
def edit_email_in_rec(book:AddressBook, args:list):
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

# 
def del_email_in_rec(book:AddressBook, args:list):
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