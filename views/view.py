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
        # if answer == "1":
        
        
def view_notes(notes):
    for note in notes:
        print(note)