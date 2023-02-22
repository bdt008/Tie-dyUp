from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import ProductForm, ReviewForm
from app.models import db, Product, User, Review, Store
from sqlalchemy.orm import joinedload
from datetime import datetime

product_routes = Blueprint('products', __name__)

# get all products
@product_routes.route('/')
def get_all_products():
    products = Product.query.order_by(Product.created_date.desc()).all()
    return jsonify([product.to_dict() for product in products]), 200

#get a single product
@product_routes.route('/<int:product_id')
def get_product(product_id):
    product = Product.query.filter(product.id == product_id).first()
    if product:
        product_obj = product.full_product_to_dict()
        return jsonify(product_obj), 200
    else:
        return jsonify({'Message': 'Product could not be found'}), 400

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

#edit an item
@product_routes.routes('/<int:product_id>', methods = ['PUT'])
@login_required
def edit_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        product.name = form.data['name']
        product.description = form.data['description']
        product.price = form.data['price']
        product.image_url = form.data['image_url']
        product.brand = form.data['brand']
        product.category = form.data['category']
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 200
    else:
        return jsonify({'errors': form.errors}), 400

#delete an item
@product_routes.route('/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200


#get review for product
# @product_routes.route('/<int:product_id>/reviews')
# def get_item_reviews(item_id):
#   product = Product.query.get(item_id)
#   if product:
#     reviews = [review.to_dict() for review in product.product_reviews]
#     return jsonify({ 'Reviews': reviews}), 200
#   else:
#     return jsonify({'message': 'Item could not be found'}), 404
