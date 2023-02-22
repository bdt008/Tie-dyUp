from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Cart, Product, User, Cart_Item
from sqlalchemy.orm import joinedload
from datetime import datetime

cart_routes = Blueprint('carts', __name__)

#create a cart
@cart_routes.route('/', methods=['POST'])
@login_required
def create_cart():
    if current_user:
        cart = Cart(
            user_id=current_user.id
        )
        db.session.add(cart)
        db.session.commit()
        return cart.to_dict()

# get a cart by id
@cart_routes.route('/<int:cart_id>')
def get_one_store(cart_id):
    cart = Cart.query.filter(Cart.id == cart_id).first()
    if cart:
        if cart.user_id == current_user.id:
            cart_obj = cart.to_dict()
            return jsonify(cart_obj), 200
        else:
            return jsonify({'message': 'Cart could not be found'}), 404

# add an item to a cart
@cart_routes.route('/<int:cart_id>/add_item/<int:item_id>', methods=['POST'])
@login_required
def add_product(cart_id, product_id):
    cart = Cart.query.filter(Cart.user_id == current_user.id, Cart.check_out == False).first()
    product = Product.query.filter(Product.id == product_id).first()

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if not cart:
        if cart.user_id == current_user.id:
            cart = Cart(user_id = current_user.id)
            cart_item = Cart_Item(
                cart_id = cart_id,
                item_id = product_id
            )
            db.session.add(cart)
            db.session.add(cart_item)
            db.session.commit()
            return jsonify(cart.to_dict()), 200
        else:
            return jsonify({'message': 'Users can only add items to their own cart'}), 403
    else:
        return jsonify({'message': 'Cart could not be found'}), 404

# delete item from cart
@cart_routes.route('/<int:cart_id>/deleteItem/<int:product_id>', methods=['DELETE'])
@login_required
def delete_item_from_cart(cart_id, product_id):
    if request.method == 'DELETE':
        cart = Cart.query.filter(Cart.id == cart_id).first()
        product = Product.query.filter(Product.id == product_id).first()
        cart_item = Cart_Item.query.filter(Cart_Item.product_id == product.id, Cart_Item.cart_id == cart.id).first()
        if cart:
            if product:
                if cart_item:
                    if cart.user_id == current_user.id:
                        db.session.delete(cart_item)
                        db.session.commit()
                        return jsonify({'message': 'Successfully deleted', 'cart': cart.to_dict()}), 200
                    else:
                        return jsonify({'message': 'Users can only delete items in their own cart'}), 403
                else:
                    return jsonify({'message': 'Product is not in this cart'}), 403
            else:
                return jsonify({'message': 'Product could not be found'}), 404
        else:
            return jsonify({'message': 'Cart could not be found'}), 404

#update cart
@cart_routes.route('/<int:cart_id>/update', methods=['PUT'])
@login_required
def update_cart_status(cart_id):
    if request.method == 'PUT':
        cart = Cart.query.filter(Cart.id == cart_id).first()
        if cart:
            if cart.user_id == current_user.id:
                cart.checked_out = True
                db.session.add(cart)
                db.session.commit()
                return jsonify(cart.to_dict()), 200
            else:
                return jsonify({'message': 'Users can only update their own cart'}), 403
        else:
            return jsonify({'message': 'Cart could not be found'}), 404

#delete an entire cart
@cart_routes.route('/<int:product_id>/delete', methods=['DELETE'])
@login_required
def delete_cart(cart_id):
        cart = Cart.query.filter(Cart.id == cart_id).first()
        if cart:
            if cart.user_id == current_user.id:
                db.session.delete(cart)
                db.session.commit()
                return jsonify({'message': 'Successfully deleted'}), 200
            else:
                return jsonify({'message': 'Users can only delete their own cart'}), 403
        else:
            return jsonify({'message': 'Cart could not be found'}), 404
