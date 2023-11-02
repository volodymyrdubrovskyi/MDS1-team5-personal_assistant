from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import datetime

# You need to install the external package in the terminal first: pip install prompt_toolkit

commands = WordCompleter([
    "close", "exit", "hello", "add", "edit", "del", 
    "add-phone", "edit-phone", "del-phone", "all", 
    "add-email", "edit-email", "del-email", 
    "birthday", "del-birthday", "next-birthdays", "note", "help"], ignore_case=True)
session = PromptSession(completer=commands)
nsession = PromptSession()

def upcoming_birthdays(book, args):
    today = datetime.date.today()
    birthday_contacts = []
    this_year = today.year

    for _, record in book.data.items():
        if record.birthday is not None:
            days_until_birthday = (record.birthday.value.replace(year=this_year) - today).days
            if 0 <= days_until_birthday <= int(args[0]):
                birthday_contacts.append(record)

    return birthday_contacts