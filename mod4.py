from classes import *

# выход, тут сохраняем AdressBook
def exit_procedure(book:AddressBook):
    book.save_to_file()
    print('Good bye!')


def add_record(book:AddressBook, args:list):
    if len(args) ==1 and len(args[0]) > 0:
        book.add_record(args[0])
    else:
        print('Error: Invalid command format.')