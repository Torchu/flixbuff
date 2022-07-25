"""Test module for the Test model."""
from api.models.test import Test

class TestTest():
    """Test class for the Test model."""

    def test_greet(self):
        """Tests the greet method."""
        test = Test()
        assert test.greet() == "Hello World!"

    def test_personal_greeting(self):
        """Tests the personal_greeting method."""
        test = Test()
        assert test.personal_greeting("John") == "Hello John!"
