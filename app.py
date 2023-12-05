from flask import Flask
from flask_cors import CORS
from fruits import fruits_bp
from vegetable import vegetables_bp
from order import orders_bp 

app = Flask(__name__)
CORS(app)


# Registering Blueprints
app.register_blueprint(fruits_bp)
app.register_blueprint(vegetables_bp)
app.register_blueprint(orders_bp)

if __name__ == '__main__':
    app.run(debug=True)
