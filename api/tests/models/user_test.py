"""Test module for the User class."""
from flask import current_app


class TestUser():
    """Test class for the User class."""

    def test_insert(self):
        """Test for the insert method."""
        a = current_app
        print(a)
