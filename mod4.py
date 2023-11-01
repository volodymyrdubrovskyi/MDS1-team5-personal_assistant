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