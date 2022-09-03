"""Module for the user schemas."""
from marshmallow import Schema, fields


class UserSchema(Schema):
    """Schema for the user model."""
    _id = fields.String(dump_only=True, required=True, description='User id')
    username = fields.Str(required=True, description='Username')
    email = fields.Email(required=True, description='Email')
    password = fields.Str(load_only=True, required=True, description='Password')
