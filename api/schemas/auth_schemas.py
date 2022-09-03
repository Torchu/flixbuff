"""Module for the auth schemas."""
from marshmallow import Schema, fields


class LoginParametersSchema(Schema):
    """Schema for the login parameters."""
    email = fields.Str(required=True, description='Email of the user')
    password = fields.Str(required=True, description='Password of the user')

    class Meta:
        strict = True


class LoginResponseSchema(Schema):
    """Schema for the login response."""
    class UserInfoSchema(Schema):
        """Info of the user given as a response."""
        id = fields.Str(description='User email')

    login_ok = fields.Boolean(description='If the login was successful')
    access_token = fields.Str(description='Access token for the user')
    user = fields.Nested(UserInfoSchema, description='Info of the user')
