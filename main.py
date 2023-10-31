from classes import *


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():

    print('Welcome to the assistant bot!')

    # Загружаем адресную книгу, если находим. 
    # Если не находим: Делаем пустую AdressBook
    try:
        abook = AddressBook().read_from_file()
    except:
        abook = AddressBook()

    
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            
            if command in ['close', 'exit']:
                # выход, тут сохраняем AdressBook
                abook.save_to_file()
                print('Good bye!')
                break

            elif command == 'hello':
                print('How can I help you?')
            
            else:
                print('Error: Invalid command.')

if __name__ == '__main__':
    main()