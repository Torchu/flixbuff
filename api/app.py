from config.flask_config import API_PORT, DEBUG_MODE, OPENAPI_CONFIG, SECRET_KEY
from config.mongodb_config import DB_NAME, DB_URI
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_rest_api import Api
from flask_pymongo import PyMongo
from services import auth_service, show_service

app = Flask(__name__)

# Set up the configurations
app.config.update(OPENAPI_CONFIG)
app.config["MONGO_URI"] = f"{DB_URI}/{DB_NAME}"
app.config["JWT_SECRET_KEY"] = SECRET_KEY

# Set up the extensions
mongo = PyMongo(app)
jwt = JWTManager(app)
api = Api(app)

# Register routes
api.register_blueprint(auth_service.blp)
api.register_blueprint(show_service.blp)


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=API_PORT)
