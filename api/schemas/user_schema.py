"""Module for the user schemas."""
import marshmallow as ma


class UserSchema(ma.Schema):
    """Schema for the user model."""
    id = ma.fields.Int(dump_only=True, required=True, description='User id')
    username = ma.fields.Str(required=True, description='Username')
    email = ma.fields.Email(required=True, description='Email')
    password = ma.fields.Str(load_only=True, required=True, description='Password')
