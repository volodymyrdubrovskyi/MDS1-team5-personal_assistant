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
    """
    Returns a list of contacts from the contact book whose birthdays are approaching.

    :param book: The contact book object where contact data is stored.

    :param args: Function arguments. args[0] specifies the number of days to consider for upcoming birthdays.

    :return: A list of contacts whose birthdays are approaching and meet the criteria.

    The function checks all contacts in the book and determines if each contact's birthday is approaching within the
    specified number of days, which is passed as the first element in `args`. If a contact's birthday is approaching,
    it is added to the `birthday_contacts` list. Contacts whose birthdays have already passed or are yet to come are
    not included in the result.

    For example, if `args[0]` is set to 7, the function will return a list of contacts whose birthdays are approaching
    within the next 7 days.
    """
    today = datetime.date.today()
    birthday_contacts = []
    this_year = today.year
    try:
        for _, record in book.data.items():
            if record.birthday is not None:
                days_until_birthday = (record.birthday.value.replace(year=this_year) - today).days
                if 0 <= days_until_birthday <= int(args[0]):
                    birthday_contacts.append(record)

        if birthday_contacts:
            return birthday_contacts
        else:
            print('There are no upcoming birthdays')
            return False
    except IndexError:
        print('Command should be followed by "number of days" parameter')
    except ValueError:
        print('"number of days" parameter should be integer')
    
    