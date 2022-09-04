"""Module for the auth schemas."""
from marshmallow import Schema, fields


class LoginParametersSchema(Schema):
    """Schema for the login parameters."""
    email = fields.Str(required=True, metadata={'description': 'Email of the user'})
    password = fields.Str(required=True, metadata={'description': 'Password of the user'})

    class Meta:
        strict = True


class LoginResponseSchema(Schema):
    """Schema for the login response."""
    class UserInfoSchema(Schema):
        """Info of the user given as a response."""
        id = fields.Str(metadata={'description': 'User ID'})
        email = fields.Email(metadata={'description': 'User email'})
        username = fields.Str(metadata={'description': 'Username'})

    login_ok = fields.Boolean(metadata={'description': 'If the login was successful'})
    access_token = fields.Str(metadata={'description': 'Access token for the user'})
    user = fields.Nested(UserInfoSchema, metadata={'description': 'Info of the user'})
