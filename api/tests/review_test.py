"""Test module for the Review model."""
import pytest
from models.review import Review, ShowInfo


class TestReview():
    """Test class for the Review model."""

    def test_initialize(self):
        """Tests the initialization of the Review model."""
        review = Review('Juan Antonio', ShowInfo('Cosas rarunas', 1, 'Season 1'), "This is a review", 10)
        assert isinstance(review, Review)

    def test_rating_exception(self):
        """Test that and exception is raised when the rating is not between 0 and 10."""
        with pytest.raises(ValueError):
            Review('Juan Antonio', ShowInfo('Cosas rarunas', 1, 'Season 1'), "This is a review", 11)
