import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.environ.get('DB_URI', 'mongodb://localhost:27017')
DB_NAME = os.environ.get('DB_NAME', 'flixbuff')
