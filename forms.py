from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message='Please enter a pet name')])
    species = SelectField("Specices", choices=[('cat', 'Cat'), ('dog', 'Dog')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=35)])
    notes = StringField("Add any notes you'd want owners to know about this pet!", validators=[Optional(), Length(min=30)])

