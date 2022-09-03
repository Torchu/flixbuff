"""Module for the user service."""
from flask_rest_api import Blueprint
from models.user import User
from schemas.user_schema import UserSchema

blp = Blueprint('User', 'user', url_prefix='/user', description='User services')


@blp.route('', methods=['POST'])
@blp.arguments(UserSchema)
@blp.response(UserSchema, code=201)
def create_user(user_data: dict) -> dict:
    """Creates a new user."""
    user = User(user_data)
    return user.insert()
