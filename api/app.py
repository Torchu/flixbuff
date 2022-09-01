from config.flask_config import API_PORT, DEBUG_MODE
from flask import Flask
from flask_rest_api import Api
from services import test_service

app = Flask(__name__)
app.config['OPENAPI_VERSION'] = '3.0.2'

api = Api(app)

api.register_blueprint(test_service.blp)

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=API_PORT)
