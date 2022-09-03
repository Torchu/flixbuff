"""Module for the user service."""
from flask_rest_api import Blueprint, abort
from models.user import User, DuplicateEmailError
from schemas.user_schema import UserSchema

blp = Blueprint('User', 'user', url_prefix='/user', description='User services')


@blp.route('', methods=['POST'])
@blp.arguments(UserSchema)
@blp.response(UserSchema, code=201)
def create_user(user_data: dict) -> dict:
    """Creates a new user."""
    user = User(user_data)
    try:
        return user.insert()
    except DuplicateEmailError as e:
        abort(e.code, message=e.message)
