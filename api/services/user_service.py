"""Module for the user service."""
from bson import ObjectId
from flask_rest_api import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, DuplicateEmailError, UserNotFoundError
from models.review import Review
from schemas.shared_schemas import QueryParametersSchema
from schemas.user_schema import UserSchema, UserListSchema
from schemas.review_schema import ReviewListSchema

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


@blp.route('/<string:user_id>/reviews', methods=['GET'])
@blp.response(ReviewListSchema, code=200)
def list_reviews_from_user(user_id: str) -> dict:
    """Returns the list of reviews from a user"""
    review_list, total = Review.list_from_user(user_id)
    return {
        "items": [review.to_json() for review in review_list],
        "total": total
    }


@blp.route('/<string:user_id>', methods=['GET'])
@blp.response(UserSchema, code=200)
def get_user(user_id: str) -> dict:
    """Returns the selected user"""
    return User.find({'_id': ObjectId(user_id)})


@blp.route('/follow/<string:user_id>', methods=['PUT'])
@blp.response(UserSchema, code=201)
@jwt_required()
def follow_user(user_id: str) -> dict:
    """Follows a user"""
    current_user = get_jwt_identity()
    user = User.find({'_id': ObjectId(current_user.get('_id'))})
    try:
        return user.follow(user_id)
    except UserNotFoundError as e:
        abort(e.code, message=e.message)


@blp.route('/unfollow/<string:user_id>', methods=['PUT'])
@blp.response(UserSchema, code=201)
@jwt_required()
def follow_user(user_id: str) -> dict:
    """Unfollows a user"""
    current_user = get_jwt_identity()
    user = User.find({'_id': ObjectId(current_user.get('_id'))})
    try:
        return user.unfollow(user_id)
    except UserNotFoundError as e:
        abort(e.code, message=e.message)
