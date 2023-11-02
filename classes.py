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
        return 'No Data' if self.value == None else self.value.strftime('%d.%m.%Y')
    
class Phone(Field):
    MAX_PHONE_LEN = 10

    def __init__(self, value):
        self.value = value

class Email(Field):
    def __init__(self, value):
        self.value = value

class Record:
    # USER_COUNTER = 0

    def __init__(self, name, book, birthday=None):
        self.user_id = book.user_id_counter
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = birthday
        self.address = ''

    # Додавання email до запису
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

    # Видаленя email з запису
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

    #
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


    # добавление объекта телефон в запись
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
        
    # удаление телефона из списка телефонов
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

    # изменение объекта телефон в записи
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
        self.data[self.user_id_counter] = record
        self.user_id_counter += 1
    
    # редактирование имени записи в адресной книге
    def edit_record(self, args):
        self.data[int(args[0])].name.value = args[1]

    # удаление записи в адресной книге
    def del_record(self, args):
        self.data.pop(int(args[0]))
from datetime import datetime

class Note:
    def __init__(self, content, tags):
        self.content = content
        self.tags = tags
        self.creation_date = datetime.now() 
        
notes = []

