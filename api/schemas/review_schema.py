"""Module for the review schema."""
from marshmallow import Schema, fields


class ReviewSchema(Schema):
    """Review schema."""
    _id = fields.Str(dump_only=True)
    reviewer_id = fields.Str(dump_only=True)
    season_info = fields.Dict(required=True)
    review = fields.Str(required=True)
    rating = fields.Int(required=True)
    date = fields.Date(dump_only=True)
