"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators=[InputRequired("Pet name can't be blank"), Length(min=3, max=20)])
    species = StringField('Species', validators=[InputRequired("Species can't be blank"), AnyOf(['cat', 'dog', 'porcupine'])])
    photo = StringField('Photo URL', validators=[Optional(), URL('Must add valid URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField('Available?')

class EditPetForm(FlaskForm):
    """For for Editing Pets"""

    photo_url = StringField('Photo URL', validators=[Optional(), URL('Must add valid URL')])    
    notes = StringField('Notes')
    available = BooleanField('Available?')

