"""Module for review service."""
from flask_rest_api import Blueprint
from models.review import Review
from schemas.review_schema import ReviewSchema

blp = Blueprint('Review', 'Review', url_prefix='/review')


@blp.route('', methods=['POST'])
@blp.arguments(ReviewSchema)
@blp.response(ReviewSchema, code=201)
def create_review(review_data: dict) -> dict:
    """Creates a new review."""
    review = Review(review_data)
    return review.insert()
