"""This module is used for the user class."""
import re
from typing import Dict, List, Tuple, Union
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
from bson import ObjectId


class DuplicateEmailError(Exception):
    """Class to define a duplicate email error."""

    def __init__(self) -> None:
        self.code = 400
        self.message = 'Email already in use'


class UserNotFoundError(Exception):
    """Class to define a user not found error."""

    def __init__(self) -> None:
        self.code = 404
        self.message = 'User no found'


class User:
    """Class that represents an user of the appication."""

    def __init__(self, data: Dict) -> None:
        """
        Constructor of the User class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - _id: User id
            - username: str
            - password: str
            - email: str
            - following: list[str]
        """
        self._id = data.get('_id')
        self.username = data.get('username')
        self.password = data.get('password')
        self.email = data.get('email')
        self.following = data.get('following', [])

    def insert(self) -> 'User':
        """
        Inserts the user into the database.
        :return: User object
        """
        # Checks if the email is already in use
        if User.find({'email': self.email}) is not None:
            raise DuplicateEmailError

        # Maps the user object to a dictionary
        data_to_insert = self.__dict__

        # Erases the ID if it exists
        if '_id' in data_to_insert:
            del data_to_insert['_id']

        # Hashes the password
        if 'password' in data_to_insert:
            data_to_insert['password'] = generate_password_hash(data_to_insert.get('password'))

        user_id = current_app.mongo.db.users.insert_one(data_to_insert).inserted_id

        # Returns the user object
        new_user = User.find({'_id': user_id})
        return new_user

    @classmethod
    def find(cls, criteria: Dict, projection: Dict = {}) -> Union['User', None]:
        """
        Finds a user in the database.
        :param criteria: Dictionary with the search criteria
        :param projection: Dictionary with the fields to return
        :return: User object
        """
        # Sets {'password': 0} as default
        if not projection.get('password'):
            projection['password'] = 0

        user_data = current_app.mongo.db.users.find_one(criteria, projection)
        return User(user_data) if user_data else None

    def check_password(self, password: str) -> bool:
        """
        Method to check the user password
        :param password: Password to check
        :return: If the given password hash matches the user password hash
        """
        # Searches agains to get the stored password
        user = User.find({'_id': self._id}, {'password': 1})
        return check_password_hash(user.password, password)

    @classmethod
    def login_user(cls, user_email: str, user_password: str) -> Tuple[Union['User', None], bool]:
        """
        This method return the user supposed to log in and the success of the process
        :param user_email: Email of the user
        :param user_password: Password of the user
        :return: An user and whether the login was successful or not
        """
        valid = False

        user = User.find({'email': user_email})
        if user is not None:
            if user.check_password(user_password):
                valid = True
        return user, valid

    @classmethod
    def validate_user(cls, user_email: str, password: str) -> Union['User', None]:
        """
        Wrapper method to validate the user, manage the general actions after login and
        return it for Flask and Basic Login (id for Flask and email for email validation)
        :param user_email: Email of the user
        :param password: Password of the user
        :return: the user
        """
        user, valid = cls.login_user(user_email=user_email, user_password=password)
        return user if valid else None

    @classmethod
    def list(cls, query: str = None) -> Tuple[List['User'], int]:
        """
        Returns the list of users
        :param query: Dictionary with the search criteria
        :return: List of users and total of users
        """
        # Sets {'password': 0} as default
        projection = {'password': 0}

        # Adds the query to the search criteria
        criteria = {'username': {'$regex': re.compile(query, flags=re.IGNORECASE)}} if query else {}

        # Searches the users
        cursor = current_app.mongo.db.users.find(criteria, projection)
        users = [User(user) for user in cursor]
        total = current_app.mongo.db.users.count_documents(criteria)

        # Returns the list of users
        return users, total

    def follow(self, user_id: str) -> 'User':
        """
        Adds a user to the following list
        :param user_id: User ID to follow
        :return: The updated user
        """
        # Checks if the user exists
        if User.find({'_id': ObjectId(user_id)}) is None:
            raise UserNotFoundError

        # Adds the user to the following list
        current_app.mongo.db.users.update_one({'_id': self._id}, {'$addToSet': {'following': user_id}})

        return User.find({'_id': self._id})

    def unfollow(self, user_id: str) -> 'User':
        """
        Removes a user from the following list
        :param user_id: User ID to unfollow
        :return: The updated user
        """
        # Checks if the user exists
        if User.find({'_id': ObjectId(user_id)}) is None:
            raise UserNotFoundError

        # Removes the user to the following list
        current_app.mongo.db.users.update_one({'_id': self._id}, {'$pull': {'following': user_id}})

        return User.find({'_id': self._id})

    def complete_info(self) -> Dict:
        """Returns a dict with the data of the user and its total reviews and followers."""
        user_data = self.__dict__
        user_data['total_reviews'] = current_app.mongo.db.reviews.count_documents(
            {'reviewer_info.reviewer_id': str(self._id)})
        user_data['total_followers'] = current_app.mongo.db.users.count_documents({'following': str(self._id)})
        return user_data
