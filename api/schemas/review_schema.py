"""Module for the review schema."""
from marshmallow import Schema, fields
from schemas.shared_schemas import generate_list_schema


class SeasonInfoSchema(Schema):
    """Schema for the season info inside the review."""
    show_id = fields.Int(required=True, metadata={'description': 'Show id'})
    show_name = fields.Str(dump_only=True, metadata={'description': 'Show name'})
    season_number = fields.Int(required=True, metadata={'description': 'Season number'})
    season_name = fields.Str(dump_only=True, metadata={'description': 'Season name'})
    season_poster = fields.Str(dump_only=True, metadata={'description': 'Season poster'})


class ReviewerInfoSchema(Schema):
    """Schema for the reviewer info inside the review."""
    reviewer_id = fields.Str(dump_only=True, metadata={'description': 'Reviewer id'})
    reviewer_username = fields.Str(dump_only=True, metadata={'description': 'Reviewer username'})


class ReviewSchema(Schema):
    """Review schema."""
    _id = fields.Str(dump_only=True, metadata={'description': 'ID'})
    reviewer_info = fields.Nested(ReviewerInfoSchema, dump_only=True, metadata={'description': 'Reviewer information'})
    season_info = fields.Nested(SeasonInfoSchema, required=True, metadata={'description': 'Season information'})
    review = fields.Str(required=True, metadata={'description': 'Review text'})
    rating = fields.Int(required=True, metadata={'description': 'Review points'})


ReviewListSchema = generate_list_schema(ReviewSchema)
