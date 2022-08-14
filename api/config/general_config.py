import os
from dotenv import load_dotenv

load_dotenv()

SHOWS_DB_API = 'https://api.themoviedb.org/3/tv'
SHOWS_DB_API_KEY = os.environ.get('SHOWS_DB_API_KEY')
SHOWS_DB_LANGUAGE = os.environ.get('SHOWS_DB_LANGUAGE', 'es_ES')

DEBUG_MODE = os.environ.get('DEBUG_MODE', True)
API_PORT = os.environ.get('API_PORT', 5000)
