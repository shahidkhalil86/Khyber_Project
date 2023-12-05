from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

fruits_bp = Blueprint('fruits', __name__)

# MongoDB Configuration
mongo = MongoClient('mongodb://localhost:27017/khyber')
db = mongo.get_database()

@fruits_bp.route('/fruits', methods=['GET'])
def get_fruits():
    try:
        # Access the 'fruits' collection
        fruits_collection = db['fruits']

        # Find all documents in the collection
        fruits = list(fruits_collection.find())

        # Convert the result to a list of dictionaries for JSON response
        fruit_list = []
        for fruit in fruits:
            fruit_dict = {
                'fruit_id': str(fruit['_id']),
                'name': fruit['name'],
                'category': fruit['category'],
                'price': float(fruit['price']),
                'quantity_in_stock': fruit['quantity_in_stock'],
                'description': fruit['description'],
                'imgsrc': fruit['imgsrc']
            }
            fruit_list.append(fruit_dict)

        # Return the retrieved fruits as JSON
        return jsonify(fruit_list)

    except Exception as e:
        return jsonify({'error': str(e)})

@fruits_bp.route('/fruits', methods=['POST'])
def add_fruit():
    try:
        # Get data from the request
        data = request.get_json()
        name = data['name']
        category = data['category']
        price = data['price']
        quantity_in_stock = data['quantity_in_stock']
        description = data['description']
        imgsrc = data['imgsrc']

        # Access the 'fruits' collection
        fruits_collection = db['fruits']

        # Insert the new fruit as a document
        new_fruit = {
            'name': name,
            'category': category,
            'price': price,
            'quantity_in_stock': quantity_in_stock,
            'description': description,
            'imgsrc': imgsrc
        }
        result = fruits_collection.insert_one(new_fruit)

        return jsonify({'message': 'Fruit added successfully', 'fruit_id': str(result.inserted_id)})

    except Exception as e:
        return jsonify({'error': str(e)})

@fruits_bp.route('/fruits/<string:fruit_id>', methods=['DELETE'])
def delete_fruit(fruit_id):
    try:
        # Access the 'fruits' collection
        fruits_collection = db['fruits']

        # Delete the fruit by _id
        result = fruits_collection.delete_one({'_id': ObjectId(fruit_id)})

        if result.deleted_count > 0:
            return jsonify({'message': 'Fruit deleted successfully'})
        else:
            return jsonify({'message': 'Fruit not found'})

    except Exception as e:
        return jsonify({'error': str(e)})
