from controller import work_with_notes


def view_menu():
    work_with_notes.start_app()
    print("Вас приветствует записная книжка!")
    is_running = True
    while is_running:
        print("Меню:"
              "\n1.Показать заметки"
              "\n2.Показать заметки по фильтру"
              "\n3.Добавить заметку"
              "\n4.Редактировать заметку"
              "\n5.Удалить заметку"
              "\n0.Выход")
        answer = input("Введите номер операции:")
        if answer == "1":
            view_notes()
        elif answer == "2":
            view_filter_note()
        elif answer == "3":
            view_add_note()
        elif answer == "4":
            update_note()
        elif answer == "5":
            del_note(input("Введите ID заметки:"))
        elif answer == "0":
            is_running = False


def view_notes():
    work_with_notes.print_notes()


def view_filter_note():
    print("Выберите вид фильтра:"
          "\n1.Фильтровать по ID"
          "\n2.Фильтровать по заголовку заметки"
          "\n3.Фильтровать по тексту заметки"
          "\n4.Фильтровать по дате"
          "\n0.Назад")
    answer = input("Введите номер операции:")
    if answer == "1":
        id = input("Введите ID: ")
        work_with_notes.print_notes_on_id(id)
    elif answer == "2":
        head = input("Введите заголовок: ")
        work_with_notes.print_notes_on_head(head)
    elif answer == "3":
        text = input("Введите текст: ")
        work_with_notes.print_notes_on_text(text)
    elif answer == "4":
        data = input("Введите дату(Прмер 2023-05-13 13:12:16): ")
        work_with_notes.print_notes_on_data(data)


def view_add_note():
    head = input("Введите заголовок заметки:")
    text = input("Введите заметку:")
    work_with_notes.add_note(head, text)


def update_note():
    id = input("Введите ID заметки которую хотите изменить:")
    work_with_notes.print_notes_on_id(id)
    head = input("Введите новый заголовок заметки:")
    text = input("Введите новую заметку:")
    work_with_notes.change_note(id, head, text)


def del_note(id):
    work_with_notes.remove_note(id)
    print("Заметка ID=" + id + " удалена.")
