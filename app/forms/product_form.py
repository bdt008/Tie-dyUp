from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.models import Product

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    image_url = StringField('Product Image Url', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    catagory = SelectField('Catagory', choices=['shirt', 'pants', 'dress', 'shoes', 'jewelry'], validators=[DataRequired()])
    submit = SubmitField('Post Product')
