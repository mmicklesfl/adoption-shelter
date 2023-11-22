from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()

toolbar = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/") 
def list_pets():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'submit' and k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    else:
        return render_template("form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))

    else:
        form.name.data = pet.name
        form.species.data = pet.species
        form.age.data = pet.age
        return render_template("edit.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}
    return jsonify(info)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
