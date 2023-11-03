from classes import *

# выход, тут сохраняем AdressBook
def exit_procedure(book:AddressBook):
    book.save_to_file()
    print('Good bye!')

# Создаем запись контакта
def add_record(book:AddressBook, args:list):
    if len(args) ==1:
        book.add_record(Record(args[0], book))
        print('Record created sucessfully')
    else:
        print('Error: Invalid command format.')

# редактирование имени контакта
def edit_record(book:AddressBook, args:list):
    if len(args) ==1:
        if int(args[0]) in book.data:
            book.del_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

# удаление контакта
def del_record(book:AddressBook, args:list):
    if len(args) ==1:
        if int(args[0]) in book.data:
            book.del_record(args)
            print('Record sucessfully deleted')
        else:
            print(f'Contact id {args[0]} not found')
    else:
        print('Error: Invalid command format.')

# Добавляем номер телефона контакту
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

# Изменяем номер телефона контакта
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

# Удаляем номер телефона в контакте
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

# поиск
def find_in_records(book:AddressBook, args:list):
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

# help
def show_help():
    commands = [['Command', 'Parameters', 'Description'],
                   ['all', '', 'list all information about users'],
                   ['add', '[Name]', 'create new user [Name] in adress book'], 
                   ['edit', '[Contact_id] [new_Name]', 'edit name of [Contact_id] to [new_Name]'],
                   ['del', '[Contact_id]', 'remove user [Contact_id] from adress book'],
                   ['add-phone', '[Contact_id] [Phone]', 'add to user [Contact_id] a [Phone]'],
                   ['edit-phone', '[Contact_id] [Phone] [new_Phone]', 'replace for user [Contact_id] a [Phone] by [new_Phone]'],
                   ['del-phone', '[Name] [Phone]', 'remove phone [Phone] from user [Name]'],
                   ['add-email', '[Contact_id] [Email]', 'add to user [Contact_id] an [Email]'],
                   ['edit-email', '[Contact_id] [Email] [new_Email]', 'replace for user [Contact_id] an [Email] by [new_Email]'],
                   ['del-email', '[Contact_id] [Email]', 'remove email [Email] from user [Contact_id]'],
                   ['address', '[Contact_id] [Address]', 'set for user [Name] an address [Address]'],
                   ['del-address', '[Contact_id]', 'remove address from [Contact_id]'],
                   ['birthday', '[Contact_id] [Birthday]', 'set for user [Contact_id] a birthday at [Birthday]'],
                   ['del-birthday', '[Contact_id]', 'remove birthday from [Contact_id]'],
                   ['find', '[serchstring]', 'list all users with [serchstring] data in Name, Phones, Address, Emails, Birthdays. [serchstring] must be 2 symbols minimum'],
                   ['next-birthdays', '[int]', 'shows upcoming birthdays if exist in period from today till [int] days'],
                   ['close, exit', '', 'exit the bot'],
                   ['note', '', 'switch to note functional'],
                   ['help', '', 'list all bot commands']]
    dashes = "{0:<14} + {1:<32} + {2:^12} \n".format("-" * 14, "-" * 32, "-" * 12)
    help_string = ''

    for i in commands:
        help_string += f'{i[0]:^14} | {i[1]:^32} | {i[2]:^12} \n'
        help_string += dashes
    
    print(help_string)