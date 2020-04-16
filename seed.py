from models import Pet, db
from app import app


db.drop_all()
db.create_all()

pet1 = Pet(name='Junior', species='dog', age=3, notes='He dog')
pet2 = Pet(name='Bobby', species='cat', age=10, notes='Fluffy cat')

db.session.add_all([pet1, pet2])
db.session.commit()