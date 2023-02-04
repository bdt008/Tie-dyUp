from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime

class Cart_Item(db.Model):
    __tablename__ = 'cart_items'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    product_total = db.Column(db.Decimal, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    my_cart = db.relationship("Cart", back_populates = 'cart_list')
    items_in_cart = db.relationship("Product", back_populates = 'cart_items')


    def cart_item_to_dict(self):
        return {
            'id': self.id,
            'Item': self.items_in_cart.cart_item_to_dict()
        }
