"""Test module for the User class."""
import pytest
from models.user import User, DuplicateEmailError, UserNotFoundError


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

    def test_list(self):
        """Test for the list method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user.insert()

        user = User({'username': 'Juan Luis', 'password': 'test', 'email': 'juan@luis.com'})
        user.insert()

        users, total = User.list()
        assert total == 2, 'The total number of users is not correct'
        assert len(users) == 2, 'The number of users is not correct'
        assert users[0].password is None, 'The password should not be shown'

        users, total = User.list('tes')
        assert total == 1, 'Query not applying to total'
        assert len(users) == 1, 'Query not applying to list'

    def test_follow(self):
        """Test for the follow method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user = user.insert()

        user2 = User({'username': 'Juan Luis', 'password': 'test', 'email': 'test2@test.com'})
        user2 = user2.insert()

        user = user.follow(str(user2._id))
        assert user.following == [str(user2._id)], 'The user was not followed'

        with pytest.raises(UserNotFoundError):
            user.follow('000000000000000000000000')

    def test_unfollow(self):
        """Test for the unfollow method."""
        user = User({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
        user = user.insert()

        user2 = User({'username': 'Juan Luis', 'password': 'test', 'email': 'test2@test.com'})
        user2 = user2.insert()

        user = user.follow(str(user2._id))

        user = user.unfollow(str(user2._id))
        assert user.following == [], 'The user was not unfollowed'

        with pytest.raises(UserNotFoundError):
            user.unfollow('000000000000000000000000')
