rom classes import *
from mod4 import *
from mod2 import session
from mod3 import *


# считываем с терминала команду
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():

    print('Welcome to the assistant bot!')

    # Загружаем адресную книгу, если находим. 
    # Если не находим: Делаем пустую AdressBook
    try:
        book = AddressBook().read_from_file()
    except:
        book = AddressBook()

    
    while True:
        user_input = session.prompt("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            
            if command in ['close', 'exit']:
                exit_procedure(book)
                break

            elif command == 'hello':
                print('How can I help you?')

            elif command == 'add':
                add_record(book, args)

            elif command == 'edit':
                edit_record(book, args)

            elif command == 'del':
                del_record(book, args)

            elif command == 'add-phone':
                add_phone_in_rec(book, args)
            
            elif command == 'edit-phone':
                edit_phone_in_rec(book, args)

            elif command == 'del-phone':
                del_phone_in_rec(book, args)

            elif command == 'add-email':
                add_email_in_rec(book, args)
            
            elif command == 'edit-email':
                edit_email_in_rec(book, args)

            elif command == 'del-email':
                del_email_in_rec(book, args)

            elif command == 'birthday':
                birthday_record(book, args)

            elif command == 'del-birthday':
                del_birthday(book, args)

            elif command == 'address':
                address_record(book, args)

            elif command == 'del-address':
                del_address(book, args)

            elif command == 'all':
                for _, record in book.data.items():
                    print(record)
            else:
                print('Error: Invalid command.')

if __name__ == '__main__':
    main()
