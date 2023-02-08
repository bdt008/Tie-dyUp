from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import ProductForm, ReviewForm
from app.models import db, Product, User, Review, Store
from sqlalchemy.orm import joinedload
from datetime import datetime

product_routes = Blueprint('products', __name__)

# get all products
@product_routes.route('/'):
def get_all_products():
    products = Product.query.order_by(Product.created_date.desc()).all()
    return jsonify([product.to_dict() for product in products]), 200

# create a product listing
@product_routes.route('/', methods = ['POST'])
@login_required
def product_listing():
    form = ProductForm(request.form)
    if not current_user.get_store_id() == "null":
        if form.validate_on_submit():
            product = Product(
                name = form.name.data,
                description = form.description.data,
                price = form.price.data,
                image_url = form.image_url.data,
                brand = form.brand.data,
                catagory = form.catagory.data,
                store_id = current_user.get_store_id()
            )
            db.session.add(product)
            db.session.commit()
            return jsonify(product.to_dict()), 201
        return jsonify({'message': 'Product could not be created'}), 400
