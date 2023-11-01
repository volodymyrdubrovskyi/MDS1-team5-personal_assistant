from classes import *
from mod1 import *
if __name__ == '__main__':
    assistant = PersonalAssistant()
    notes_manager = NotesManager()

    while True:
        print("1. Додати контакт")
        print("2. Пошук контактів за іменем")
        print("3. Вивести контакти з найближчими днями народження")
        print("4. Нотатки")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            # Додавання контакту
            pass

        elif choice == '2':
            # Пошук контактів за іменем
            pass

        elif choice == '3':
            # Виведення найближчих днів народження
            pass

        elif choice == '4':
            while True:
                print("1. Додати нотатку")
                print("2. Пошук нотаток за тегом")
                print("3. Показати всі нотатки")
                print("4. Редагувати нотатку")
                print("5. Видалити нотатку")
                print("6. Повернутися до головного меню")

                notes_choice = input("Виберіть опцію для нотаток: ")

                if notes_choice == '1':
                    # Додавання нової нотатки
                    pass

                elif notes_choice == '2':
                    # Пошук нотаток за тегом
                    pass

                elif notes_choice == '3':
                    # Виведення всіх існуючих нотаток
                    pass

                elif notes_choice == '4':
                    # Редагування вибраної нотатки
                    pass

                elif notes_choice == '5':
                    # Видалення вибраної нотатки
                    pass

                elif notes_choice == '6':
                    break

        elif choice == '5':
            break
