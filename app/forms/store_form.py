from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Store

class StoreEditorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    about= StringField('About', validators=[DataRequired()])
    cover_image_url = StringField('Cover Image Url')
    cover_image_url = StringField('Store Cover Image Url')
    submit = SubmitField('Open Store')
