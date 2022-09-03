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
