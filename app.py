from flask import Flask
from flask_cors import CORS
from fruits import fruits_bp
from vegetable import vegetables_bp
from order import orders_bp
from pymongo import MongoClient
from flask_pymongo import PyMongo 

app = Flask(__name__)
CORS(app)
# MongoDB Configuration
mongo = MongoClient('mongodb+srv://shahid:Password123@cluster0.46rjimq.mongodb.net/khyber?authMechanism=DEFAULT')
db = mongo.get_database()

# Registering Blueprints
app.register_blueprint(fruits_bp)
app.register_blueprint(vegetables_bp)
app.register_blueprint(orders_bp)

if __name__ == '__main__':
    app.run(debug=True)
