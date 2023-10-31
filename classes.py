from collections import UserDict
import re
import datetime
import pickle


# обработка ошибки количества символов в номере телефона
class LenPhoneError(Exception):
    pass

# обработка ошибки не числового номера телефона
class TypePhoneError(Exception):
    pass

# обработка ошибки не нахождения телефона
class PhoneNotFindError(Exception):
    pass

# обработка ошибки не нахождения записи
class RecordNotFindError(Exception):
    pass

# обработка неправильного формата даты
class DateFormatError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Birthday:
    def __init__(self, date=None):
            result = re.findall(r'\d\d.\d\d.\d\d\d\d', date)
            if result:
                self.value = datetime.date(year=int(date[6:10]), month=int(date[3:5]), day=int(date[0:2]))
            else:
                raise DateFormatError

    def add_bday(self, date):
        result = re.findall(r"\d\d.\d\d.\d\d\d\d", date)
        if not result:
            raise DateFormatError
        else:
            self.value = datetime.date(year=int(date[6:10]), month=int(date[3:5]), day=int(date[0:2]))

    def __str__(self) -> str:
        return 'No Data' if self.bday == None else self.bday.strftime('%d.%m.%Y')
    
class Phone(Field):
    MAX_PHONE_LEN = 10

    def __init__(self, value):
        self.value = value

class Email(Field):
    def __init__(self, value):
        self.value = value

class Record:
    def __init__(self, name, birthday=None):
        self.user_id = None
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = birthday
        self.address = ''

    # добавление обїекта телефон в запись
    def add_phone(self, phone):
        pass
        
    # удаление телефона из списка телефонов
    def remove_phone(self, phone):
        pass

    # изменение обїекта телефон в записи
    def edit_phone(self, phone_old, phone_new):
        pass

    # поиск номера телефона в текущей записи
    def find_phone(self, phone):
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def __init__(self):
        self.user_id_counter = 0
        self.data = UserDict()

    def read_from_file(self):
        with open('abook.dat', 'rb') as fh:
            return pickle.load(fh)

    def save_to_file(self):
        with open('abook.dat', 'wb') as fh:
            pickle.dump(self, fh)
    
    # добавление записи в словарь адресной книги
    def add_record(self, record):
        self.data[record.name.value] = record
        