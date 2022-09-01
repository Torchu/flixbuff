from config.flask_config import API_PORT, DEBUG_MODE
from config.mongodb_config import DB_NAME, DB_URI
from flask import Flask
from flask_rest_api import Api
from flask_pymongo import PyMongo
from services import test_service

app = Flask(__name__)
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config["MONGO_URI"] = f"{DB_URI}/{DB_NAME}"

mongo = PyMongo(app)
api = Api(app)

api.register_blueprint(test_service.blp)

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=API_PORT)
