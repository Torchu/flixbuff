"""Module for authentication service."""
from flask_rest_api import Blueprint
from flask.views import MethodView
from schemas.auth_schemas import LoginParametersSchema, LoginResponseSchema
from utils.auth_utils import authenticate_user


blp = Blueprint('Auth', 'auth', url_prefix='/auth', description='Authentication services')


@blp.route('/login')
class Login(MethodView):
    @blp.arguments(LoginParametersSchema)
    @blp.response(LoginResponseSchema)
    def post(self, params):
        return authenticate_user(email=params.get('email'), password=params.get('password'))
