"""Module for authentication functions."""
from flask_jwt_extended import create_access_token
from flask_pymongo import json_util
from models.user import User


def authenticate_user(email: str, password: str) -> dict:
    """
    Method to authenticate an user.
    :param email: Email of the user
    :param password: Password of the user
    :return: A dict with the result of the login
    """
    user = User.validate_user(user_email=email, password=password)

    # If the user is valid, logs the user
    if user is not None:
        user_info = {'id': user.email}
        result = {'login_ok': True, 'access_token': create_access_token(identity=user), 'user': user_info}
    else:
        result = {'login_ok': False}

    return result
