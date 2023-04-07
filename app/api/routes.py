from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Product, product_schema, products_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/products', methods = ['POST'])
@token_required
def create_product(current_user_token):
    product_code = request.json['product_code']
    date = request.json['date']
    quantity = request.json['quantity']

    user_token = current_user_token
    print(user_token)

    product = Product(product_code, date, quantity, user_token=user_token)

    db.session.add(product)
    db.session.commit()

    response = product_schema.dump(product)
    return jsonify(response)
@api.route('/products', methods = ['GET'])
@token_required
def get_product(current_user_token):
    a_user = current_user_token
    products = Product.query.filter_by(user_token = a_user).all()
    response = products_schema.dump(products)
    return jsonify(response)

@api.route('/products/<id>', methods = ['GET'])
@token_required
def get_single_product(current_user_token, id):
    product = Product.query.get(id)
    response = product_schema.dump(product)
    return jsonify(response)

# Update endpoint
@api.route('/products/<id>', methods = ['POST', 'PUT'])
@token_required
def update_product(current_user_token, id):
    product = Product.query.get(id)

    product.product_code = request.json['product_code']
    product.date = request.json['date']
    product.quantity = request.json['quantity']

    product.user_token = current_user_token

    db.session.commit()
    response = product_schema.dump(product)
    return jsonify(response)

# Delete endpoint
@api.route('/products/<id>', methods = ['DELETE'])
@token_required
def delete_product(current_user_token, id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    response = product_schema.dump(product)
    return jsonify(response)
