from datetime import datetime
import json


class Notes():
    def __init__(self, id_notes, text, data=datetime.now()):
        self.id_notes = id_notes
        self.text = text
        self.data = data

    def init_json(self, json_data):
        self.__dict__ = json.loads(json_data)
    
    def __str__(self):
        return f'id: {self.id_notes}\n Текст заметки: {self.text}\n Дата создания: {self.data}\n'
    
    def to_list_notes(self):
        return [self.id_notes, self.text, self.data]
    
    def to_JSON(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True)
    
    def to_dict(self):
        return {'id': self.id_notes, 'text': self.text, 'data': self.data}