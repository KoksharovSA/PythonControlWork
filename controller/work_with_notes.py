import json

from controller import settings
from data import database_collection
from models import notes


def start_app():
    database_collection.db = db_load(settings.directory_db_notes)


def add_note(head, text):
    database_collection.db.append(notes.Notes(id_note=notes.Notes.next_id([x.id_note for x in database_collection.db]),
                                              head=head, text=text))


def print_notes():
    for note in database_collection.db:
        print(note)


def print_notes_on_id(id):
    [print(x) for x in database_collection.db if int(x.id_note) == int(id)]


def print_notes_on_head(head):
    [print(x) for x in database_collection.db if head in x.head]


def print_notes_on_text(text):
    [print(x) for x in database_collection.db if text in x.text]


def print_notes_on_data(data):
    [print(x) for x in database_collection.db if data in x.data]


def remove_note(id):
    database_collection.db.remove([x for x in database_collection.db if int(x.id_note) == int(id)][0])
    db_load(settings.directory_db_notes)


def change_note(id, head, text):
    remove_note(id)
    database_collection.db.append(notes.Notes(id_note=id, head=head, text=text))


def db_load(path):
    with open(path, 'r') as file:
        db_collection = json.loads(file.read())
    return [notes.Notes.json_to_note(x) for x in db_collection]


def db_upload(path, db):
    with open(path, 'w') as file:
        file.write(json.dumps(db, default=lambda x: x.__dict__))


def db_update(path, db):
    db_from_file = db_load(path)
    for item in db:
        if next((x for x in db_from_file if x.id_note == item.id_note), None) == None:
            db_from_file.append(item)
    db_upload(path, db_from_file)
