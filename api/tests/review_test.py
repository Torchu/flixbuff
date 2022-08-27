"""Test module for the Review model."""
import pytest
from models.review import Review, ReviewerInfo, ShowInfo


class TestReview():
    """Test class for the Review model."""

    def test_initialize(self):
        """Tests the initialization of the Review model."""
        review = Review(1, ReviewerInfo(1, 'Juan Antonio'),
                        ShowInfo(1, 'Cosas rarunas', 1, 'Season 1'), "This is a review", 10)
        assert isinstance(review, Review)

    def test_rating_exception(self):
        """Test that and exception is raised when the rating is not between 0 and 10."""
        with pytest.raises(ValueError):
            Review(1, ReviewerInfo(1, 'Juan Antonio'),
                   ShowInfo(1, 'Cosas rarunas', 1, 'Season 1'), "This is a review", 11)
