from forms import AddPetForm, EditPetForm
from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickensrawesome"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Redirects to users page"""

    # pets = Pet.query.all()
    available_pets = Pet.query.filter(Pet.available == True).all()
    unavailable_pets = Pet.query.filter(Pet.available == False).all()

    return render_template('home.html', avail=available_pets, unavail=unavailable_pets)

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""

    return render_template('404.html')    

@app.route('/add', methods=["GET", "POST"])
def add_pet():  
    """Shows form for adding a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes, available=available)

        try:
            db.session.add(new_pet)
            db.session.commit()
            flash('Created new pet')
            return redirect('/')
        except:
            db.session.rollback()
            flash('problem')
            return redirect('/add')
    else:
        return render_template('add_pet.html', form=form)  

@app.route('/<int:pet_id>', methods=["GET", "POST"])    
def display_info(pet_id):
    """Displays info about a specific pet"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        try:
            db.session.commit()
            flash('Edited Pet')
            return redirect('/')
        except:
            db.session.rollback()
            flash('problem editing')
            return redirect(f'/{pet_id}')

    else:
        return render_template('pet_info.html', pet=pet, form=form)




    