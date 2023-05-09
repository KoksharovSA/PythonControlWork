from models import notes

def view_menu():
    print("Вас приветствует записная книжка!")
    is_running = True
    while is_running:
        print("Меню:"
              "\n1.Показать заметки"
              "\n2.Добавить заметку"
              "\n3.Редактировать заметку"
              "\n4.Удалить заметку"
              "\n5.Выход")
        answer = input("Введите номер операции:")
        if answer == "1":
            ns = {notes.Notes(id_notes=1,text="qqq"), notes.Notes(id_notes=2,text="www")}
            view_notes(ns)
        
        
def view_notes(notes):
    for note in notes:
        print(note.to_JSON())
        # print(note.init_json(note.to_JSON()))
        print(note)