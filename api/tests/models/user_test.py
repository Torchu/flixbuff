"""Test module for the User class."""
import pytest
from models.user import User, DuplicateEmailError


class TestUser():
    """Test class for the User class."""

    def test_insert(self):
        """Test for the insert method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        assert user.insert() is not None, 'The user was not inserted'

        user2 = User({'username': 'test2', 'password': 'test', 'email': 'test@test.com'})
        with pytest.raises(DuplicateEmailError):
            user2.insert()

    def test_find(self):
        """Test for the find method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user.insert()

        assert User.find({'username': 'test'}) is not None, 'The user was not found'
        assert User.find({'username': 'test2'}) is None, 'Unexisting user was found'

    def test_check_password(self):
        """Test for the check_password method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user.insert()

        assert user.check_password('test') is True, 'The password is not correct'
        assert user.check_password('test2') is False, 'The wrong password was accepted'

    def test_login_user(self):
        """Test for the login_user method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user.insert()

        user, valid = User.login_user('test@test.com', 'test')
        assert user is not None, 'The user was not found'
        assert valid is True, 'The password is not correct'

        user, valid = User.login_user('test@test.com', 'test2')
        assert user is not None, 'The user was not found'
        assert valid is False, 'The wrong password was accepted'

        user, valid = User.login_user('test2@test.com', 'test')
        assert user is None, 'Unexisting user was found'
        assert valid is False, 'An unexisting user was validated'

    def test_validate_user(self):
        """Test for the validate_user method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user.insert()

        user = User.validate_user('test@test.com', 'test')
        assert user is not None, 'The user was not validated'

        user = User.validate_user('test2@test.com', 'test')
        assert user is None, 'The wrong user was validated'

        user = User.validate_user('test@test.com', 'test2')
        assert user is None, 'A wrong password was validated'
