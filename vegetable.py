from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

vegetables_bp = Blueprint('vegetables', __name__)

# MongoDB Configuration
mongo = MongoClient('mongodb://localhost:27017/khyber')
db = mongo.get_database()

@vegetables_bp.route('/vegetables', methods=['GET'])
def get_vegetables():
    try:
        # Access the 'vegetables' collection
        vegetables_collection = db['vegetables']

        # Find all documents in the collection
        vegetables = list(vegetables_collection.find())

        # Convert the result to a list of dictionaries for JSON response
        vegetable_list = []
        for vegetable in vegetables:
            vegetable_dict = {
                'vegetable_id': str(vegetable['_id']),
                'name': vegetable['name'],
                'category': vegetable['category'],
                'price': float(vegetable['price']),
                'quantity_in_stock': vegetable['quantity_in_stock'],
                'description': vegetable['description'],
                'imgsrc': vegetable['imgsrc']
            }
            vegetable_list.append(vegetable_dict)

        # Return the retrieved vegetables as JSON
        return jsonify(vegetable_list)

    except Exception as e:
        return jsonify({'error': str(e)})
