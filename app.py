from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet, db, connect_db
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "sam123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Home page, display pet name, photo, & available"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_a_pet():
    """Form for adding a pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        """when submitting form"""
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # create an add pet submit
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        """showing form"""
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>')
def show_pet_info(pet_id):
    """Show more information about a specific pet"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet-details.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    """Form for editing a pre-exisiting pet"""
    # since we're getting an id, from the db, we need to set the obj to pet within the form
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        # pet = Pet(photo_url=photo_url, notes=notes, available=available)
        # db.session.add(pet)
        db.session.commit()

        return redirect(f"/{pet_id}")
    else:
        """show form"""
        return render_template('pet-edit.html', pet=pet, form=form)