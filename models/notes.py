from datetime import datetime
import json

class Notes():
    def __init__(self, id, text, data = datetime.now()):
        self.id = id
        self.text = text
        self.data = data
    
    
    def __str__(self):
        return f'id: {self.id}\n Текст заметки: {self.text}\n Дата создания: {self.data}\n'
    
    def to_list_notes(self):
        return [self.id, self.text, self.data]
    
    def to_JSON(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True)
    
    def to_dict(self):
        return {'id': self.id, 'text': self.text, 'data': self.data}