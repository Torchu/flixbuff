from config.flask_config import API_PORT, DEBUG_MODE, ENABLE_CORS, OPENAPI_CONFIG, SECRET_KEY
from config.mongodb_config import DB_NAME, DB_URI
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_rest_api import Api
from flask_pymongo import PyMongo
from models.json_encoder import CustomJSONEncoder
from services import auth_service, show_service, user_service, review_service

app = Flask(__name__)

# Sets up the configurations
app.config.update(OPENAPI_CONFIG)
app.config["MONGO_URI"] = f"{DB_URI}/{DB_NAME}"
app.config["JWT_SECRET_KEY"] = SECRET_KEY

# Sets up the extensions
app.mongo = PyMongo(app)
jwt = JWTManager(app)
api = Api(app)

# Sets up JSON encoder
app.json_encoder = CustomJSONEncoder

# Enable CORS for Local and Test environments
if ENABLE_CORS:
    CORS(app)

# Register routes
api.register_blueprint(auth_service.blp)
api.register_blueprint(show_service.blp)
api.register_blueprint(user_service.blp)
api.register_blueprint(review_service.blp)


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=API_PORT)
