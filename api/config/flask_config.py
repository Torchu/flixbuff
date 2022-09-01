import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.environ.get('DEBUG_MODE', True)
API_PORT = os.environ.get('API_PORT', 5000)
