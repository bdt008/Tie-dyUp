from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import store_form
from app.models import db, User, Store
from sqlalchemy.orm import joinedload
from datetime import datetime

store_routes = Blueprint('stores', __name__)

# get all stores
@store_routes.route('/stores')
def get_stores():
    stores = Store.query.all()
    return jsonify([store.to_dict() for store in stores])

# create a store
@store_routes.route('/', methods = ['POST'])
@login_required
def create_store():
    form = store_form()
    form['csrf_token'].data = request.cookies['csrf_token']
    if current_user.get_store_id() == "null":
        if form.validate_on_submit():
            store = Store(
                user_id = current_user.id,
                name = form.data['name'],
                cover_image_url = form.data['cover_image_url'],
                about = form.data['about']
            )
        db.session.add(store)
        db.session.commit()
        return store.to_dict()
    else:
        return jsonify({'message': 'Store must include a name and an about section'}), 400

# get a store
@store_routes.route('/<int:store_id')
def get_store(store_id):
    store = Store.query.filter(Store.id == store_id).first()
    if store:
        store_obj = store.to_dict()
        return jsonify(store_obj), 200
    else:
        return jsonify({'message': 'No store found'}), 404

#edit a store
@store_routes.route('<int:store_id', methods = ['PUT'])
@login_required
def update_store(store_id):
    form = store_form()
    form['csrf_token'].data = request.cookies['csrf_token']
    store = Store.query.filter(Store.id == store_id).first()
    if store:
        if store.user_id == current_user.id:
            if form.validate_on_submit():
                store.user_id=current_user.id
                store.name=form.data['name'] or store.name
                store.cover_image_url=form.data['cover_image_url'] or store.cover_image_url
                store.about=form.data['about'] or store.about
                store.updated_date = datetime.now()
                db.session.add(store)
                db.session.commit()
                return jsonify(store.to_dict()), 200

#delete a store
@store_routes.route('<int:store_id', methods = ['DELETE'])
@login_required
def delete_store(store_id):
    store = Store.query.get(store_id)
    if store:
        if store.user_id == current_user.id:
            db.session.delete(store)
            db.session.commit()
            return jsonify({'message': 'Store successfully deleted'}), 200

#get reviews for store
@store_routes.route('/<int:store_id>/reviews')
def get_store_reviews(store_id):
  store = Store.query.get(store_id)
  if store:
    return jsonify({ 'Reviews': [review.to_dict() for review in store.store_reviews]}), 200
  else:
    return jsonify({'message': 'Store could not be found'}), 404
