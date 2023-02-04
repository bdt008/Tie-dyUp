from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

# Checking if user exists
def user_exists(form, field):
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

# Checking if username is already in use
def username_exists(form, field):
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), user_exists])
    image_profile_url = StringField('Image Profile URL')
    password = StringField('password', validators=[DataRequired()])
    street_number = IntegerField('Street Number', validators=[DataRequired()])
    street_name = StringField('Street Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = IntegerField('Zip Code', validators=[DataRequired()])
    telephone = StringField('Telephone')
    submit = SubmitField('Sign Up')
