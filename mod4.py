from classes import *

# выход, тут сохраняем AdressBook
def exit_procedure(book:AddressBook):
    book.save_to_file()
    print('Good bye!')


def add_record(book:AddressBook, args:list):
    if len(args) ==1:
        book.add_record(Record(args[0]))
        print('Record created sucessfully')
    else:
        print('Error: Invalid command format.')


def add_phone_in_rec(book:AddressBook, args:list):
    if len(args) ==2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.add_phone(args[1])
                print('Contact added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except LenPhoneError:
            print('Error: Phone must be 10 symbols')
    else:
        print('Error: Invalid command format.')

def edit_phone_in_rec(book:AddressBook, args:list):
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
    else:
        print('Error: Invalid command format.')

def del_phone_in_rec(book:AddressBook, args:list):
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