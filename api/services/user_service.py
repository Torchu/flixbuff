"""Module for the user service."""
from crypt import methods
from flask_rest_api import Blueprint, abort
from models.user import User, DuplicateEmailError
from schemas.shared_schemas import QueryParametersSchema
from schemas.user_schema import UserSchema, UserListSchema

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


@blp.route('', methods=['GET'])
@blp.arguments(QueryParametersSchema, location='query')
@blp.response(UserListSchema, code=200)
def list_shows(params: dict) -> dict:
    """Returns the list of users"""
    user_list, total = User.list(params.get('query'))
    return {
        "items": [user for user in user_list],
        "total": total
    }
