from app.forms import ReviewForm
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Review, Product, Store, db
from datetime import datetime

review_routes = Blueprint('reviews', __name__)


# edit a review
@review_routes.route('/<int:review_id', methods = ['POST'])
@login_required
def update_review(review_id):
    curr_user_id = int(current_user.is_autheticated) and current_user.id
    review = Review.query.get(review_id)
    form = ReviewForm();
    if review:
        if form.validate_on_submit:
            if review.user_id == curr_user_id:
                review.content = form.data['content'] or review.content
                review.updated_date = datetime.now()
                db.session.add(review)
                db.session.commit()
                return review.to_dict(int(current_user.is_authenticated) and current_user.id)
            else:
                return {'errors': ['Unauthorized']}

# delete a single review
@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
  review = Review.query.get(review_id)
  if review:
    if review.user_id == current_user.id:
      db.session.delete(review)
      db.session.commit()
      return jsonify({"message": "Successfully deleted review"}), 200
    else:
      return {'errors': ['Unauthorized']}
  else:
    return jsonify({'message': 'Review could not be found'}), 404
