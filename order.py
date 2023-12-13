from flask import Blueprint, request, jsonify
from pymongo import MongoClient

orders_bp = Blueprint('orders', __name__)

# MongoDB Configuration
mongo = MongoClient('mongodb+srv://shahid:Password123@cluster0.46rjimq.mongodb.net/khyber?authMechanism=DEFAULT')
db = mongo.get_database()

@orders_bp.route('/api/orders', methods=['GET', 'POST'])
def handle_orders():
    if request.method == 'POST':
        data = request.json
        try:
            orders = db.orders
            order_id = orders.insert_one(data).inserted_id
            response = {'message': 'Order created successfully', 'order_id': str(order_id)}
            return jsonify(response), 201
        except Exception as e:
            response = {'error': 'Internal Server Error'}
            return jsonify(response), 500
    elif request.method == 'GET':
        try:
            orders_collection = db.orders
            orders_list = list(orders_collection.find())
            
            order_data = []
            for order in orders_list:
                order_data.append({
                    'order_id': str(order['_id']),
                    'products': order['products'],
                    'emailId': order['emailId'],
                    'eirCode': order['eirCode'],
                    'phoneNumber': order['phoneNumber'],
                    'totalPrice': order['totalPrice']
                })
            
            return jsonify(order_data), 200
        except Exception as e:
            response = {'error': 'Internal Server Error'}
            return jsonify(response), 500

# Optionally, you can have a separate route for creating orders if you prefer.
# Uncomment the code below if you want a dedicated route for order creation.

# @orders_bp.route('/api/orders', methods=['POST'])
# def create_order():
#     data = request.json
#     try:
#         orders = db.orders
#         order_id = orders.insert_one(data).inserted_id
#         response = {'message': 'Order created successfully', 'order_id': str(order_id)}
#         return jsonify(response), 201
#     except Exception as e:
#         response = {'error': 'Internal Server Error'}
#         return jsonify(response), 500
