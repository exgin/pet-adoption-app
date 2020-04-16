from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_PHOTO_URL = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS9pj2ErmXH13baxS_3FQ75uPcwMnGcOHcVKE4vFSUPZc7srjV5&usqp=CAU'

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_PHOTO_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

