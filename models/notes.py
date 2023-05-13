from datetime import datetime


class Notes():
    def __init__(self, id_note, head, text, data=datetime.now().__str__()):
        self.id_note = id_note
        self.head = head
        self.text = text
        self.data = data
    
    @staticmethod
    def json_to_note(json_dict):
        print()
        return Notes(id_note=json_dict['id_note'], head=json_dict['head'], text=json_dict['text'], data=json_dict[
            'data'])
    
    def __str__(self):
        return f'id: {self.id_note}\n Заголовок заметки: {self.head}\n Текст заметки: {self.text}\n Дата создания: {self.data}\n'
    
    def to_list_notes(self):
        return [self.id_note, self.head, self.text, self.data]
    
    @staticmethod
    def next_id(id_notes):
        return max([int(x) for x in id_notes]) + 1
