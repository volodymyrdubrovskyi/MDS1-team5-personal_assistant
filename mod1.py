class NotesManager:
    def __init__(self):
        # Ініціалізація менеджера нотаток і отримання доступу до даних помічника
        self.data = assistant.data

    def add_note(self, text):
        # Додавання нової нотатки до списку нотаток
        note = {'text': text, 'tags': []}
        self.data['notes'].append(note)
        assistant.save_data()

    def find_notes_by_tag(self, tag):
        # Пошук нотаток за вказаним тегом
        results = [note for note in self.data['notes'] if tag in note['tags']]
        return results

    def show_all_notes(self):
        # Виведення всіх існуючих нотаток
        if self.data['notes']:
            for idx, note in enumerate(self.data['notes']):
                print(f"{idx + 1}. {note['text']}")
        else:
            print("Нотаток немає.")

    def edit_note(self, note_idx, new_text):
        # Редагування вибраної нотатки
        if 0 <= note_idx < len(self.data['notes']):
            self.data['notes'][note_idx]['text'] = new_text
            assistant.save_data()
            print("Нотатку відредаговано.")
        else:
            print("Неправильний номер нотатки.")

    def delete_note(self, note_idx):
        # Видалення вибраної нотатки
        if 0 <= note_idx < len(self.data['notes']):
            del self.data['notes'][note_idx]
            assistant.save_data()
            print("Нотатку видалено.")
        else:
            print("Неправильний номер нотатки.")

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
