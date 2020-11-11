from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Listing, Category

class ListingForm(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired()
                ]
            )
    list_description = StringField('Description',
            validators = [
                DataRequired()
                ]
            )
    submit = SubmitField('Post Listing')
