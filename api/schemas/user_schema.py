"""Module for the user schemas."""
from marshmallow import Schema, fields
from schemas.shared_schemas import generate_list_schema


class UserSchema(Schema):
    """Schema for the user model."""
    _id = fields.String(dump_only=True, required=True, metadata={'description': 'User id'})
    username = fields.Str(required=True, metadata={'description': 'Username'})
    email = fields.Email(required=True, metadata={'description': 'Email'})
    password = fields.Str(load_only=True, required=True, metadata={'description': 'Password'})


UserListSchema = generate_list_schema(UserSchema)
