import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.environ.get('DEBUG_MODE', True)
API_PORT = os.environ.get('API_PORT', 5000)
API_HOST = os.environ.get('API_HOST', 'localhost')
OPENAPI_CONFIG = {
    'API_VERSION': '0.1.0',
    'OPENAPI_VERSION': '3.0.2',
    'OPENAPI_URL_PREFIX': 'apidocs',
    'OPENAPI_SWAGGER_UI_PATH': 'swagger',
    'OPENAPI_SWAGGER_UI_VERSION': '3.22.2',
    'OPENAPI_REDOC_PATH': 'redoc'
}
SECRET_KEY = os.environ.get('SECRET_KEY', '73f2f6b8ce414cdf900e5ab9b525380b')
ENABLE_CORS = os.environ.get('ENABLE_CORS', True)
