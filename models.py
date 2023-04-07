from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

# Set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()
    
class Product(db.Model):
    id = db.Column(db.String, primary_key=True)

    product_code = db.Column(db.String(50), nullable = False)
    date = db.Column(db.String(50), nullable = False)
    quantity = db.Column(db.Numeric(4,2), nullable = False)

    user_token = db.Column(db.String, nullable = False)

    def __init__(self, product_code, date, quantity, user_token, id=''):
        self.id = self.set_id()

        self.product_code = product_code
        self.date = date
        self.quantity = quantity

        self.user_token = user_token

    def __repr__(self):
        return f'{self.product_code} added'
    
    def set_id(self):
        return(secrets.token_urlsafe())
    
class ProductSchema(ma.Schema):
    class Meta:
        fields = ['id', 'product_code', 'date', 'quantity', 'user_token']

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
