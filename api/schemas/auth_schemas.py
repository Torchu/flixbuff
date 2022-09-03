"""Module for the auth schemas."""
import marshmallow as ma


class LoginParametersSchema(ma.Schema):
    """Schema for the login parameters."""
    email = ma.fields.Str(required=True, description='Email of the user')
    password = ma.fields.Str(required=True, description='Password of the user')

    class Meta:
        strict = True


class LoginResponseSchema(ma.Schema):
    """Schema for the login response."""
    class UserInfoSchema(ma.Schema):
        """Info of the user given as a response."""
        id = ma.fields.Str(description='User email')

    login_ok = ma.fields.Boolean(description='If the login was successful')
    access_token = ma.fields.Str(description='Access token for the user')
    user = ma.fields.Nested(UserInfoSchema, description='Info of the user')
