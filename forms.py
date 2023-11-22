from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField, SubmitField, HiddenField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, AnyOf

class AddPetForm(FlaskForm):
    
    name = StringField(
        "Pet Name",
        validators=[InputRequired(message="Pet name is required")]
    )
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
        validators=[
            InputRequired(message="Species is required"),
            AnyOf(["cat", "dog", "porcupine"], message="Invalid species")
        ]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Invalid URL format")]
    )
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")]
    )
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10, message="Comments must be at least 10 characters long")]
    )
    submit = SubmitField('Submit')

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Invalid URL format")]
    )
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10, message="Comments must be at least 10 characters long")]
    )
    available = BooleanField("Available?")

    # Hidden fields
    name = HiddenField()
    species = HiddenField()
    age = HiddenField()
