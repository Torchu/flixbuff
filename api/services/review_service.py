"""Module for review service."""
from flask_rest_api import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.review_schema import ReviewListSchema
from models.review import Review, SeasonNotFoundError
from models.show import RequestException
from schemas.review_schema import ReviewSchema

blp = Blueprint('Review', 'Review', url_prefix='/review')


@blp.route('', methods=['POST'])
@blp.arguments(ReviewSchema)
@blp.response(ReviewSchema, code=201)
@jwt_required()
def create_review(review_data: dict) -> dict:
    """Creates a new review."""
    try:
        review = Review(review_data)
    except ValueError as e:
        abort(400, message=str(e))
    try:
        review.add_reviewer(get_jwt_identity().get('_id'), get_jwt_identity().get('username'))
        review.complete_season_info()
    except (RequestException, SeasonNotFoundError) as e:
        abort(e.code, message=e.message)
    res = review.insert().to_json()
    return res


@blp.route('', methods=['GET'])
@blp.response(ReviewListSchema, code=200)
def get_reviews():
    """Returns all reviews."""
    review_list, total = Review.list()
    return {
        "items": [review.to_json() for review in review_list],
        "total": total
    }
