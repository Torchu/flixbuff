"""Module for the user schemas."""
from ast import dump
from marshmallow import Schema, fields
from schemas.shared_schemas import generate_list_schema


class UserSchema(Schema):
    """Schema for the user model."""
    _id = fields.String(dump_only=True, required=True, metadata={'description': 'User id'})
    username = fields.Str(required=True, metadata={'description': 'Username'})
    email = fields.Email(required=True, metadata={'description': 'Email'})
    password = fields.Str(load_only=True, required=True, metadata={'description': 'Password'})
    following = fields.List(fields.String(), dump_only=True, metadata={
                            'description': 'List of IDs of the users the user is following'})
    total_reviews = fields.Int(dump_only=True, metadata={'description': 'Total number of reviews of the user'})
    total_followers = fields.Int(dump_only=True, metadata={'description': 'Total number of followers of the user'})


UserListSchema = generate_list_schema(UserSchema)
