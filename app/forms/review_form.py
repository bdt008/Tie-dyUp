from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Review

class ReviewForm(FlaskForm):
    content = StringField('Review', validators=[DataRequired()])
    star_rating = SelectField('Star Rating', choices=[(1), (2), (3), (4), (5)], validators=[DataRequired()])
    photo = StringField('Photo')
    submit = SubmitField('Leave My Review')
