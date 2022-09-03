"""Module for the review schema."""
from marshmallow import Schema, fields


class SeasonInfoSchema(Schema):
    """Schema for the season info inside the review."""
    show_id = fields.Int(required=True, metadata={'description': 'Show id'})
    show_name = fields.Str(dump_only=True, metadata={'description': 'Show name'})
    season_number = fields.Int(required=True, metadata={'description': 'Season number'})
    season_name = fields.Str(dump_only=True, metadata={'description': 'Season name'})


class ReviewSchema(Schema):
    """Review schema."""
    _id = fields.Str(dump_only=True)
    reviewer_id = fields.Str(dump_only=True)
    season_info = fields.Dict(required=True)
    review = fields.Str(required=True)
    rating = fields.Int(required=True)
