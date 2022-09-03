"""Test module for the Review model."""
import pytest
from models.review import Review, SeasonInfo


class TestReview():
    """Test class for the Review model."""

    def test_initialize(self):
        """Tests the initialization of the Review model."""
        review = Review({
            'reviewer_id': '1',
            'season_info': {
                'show_name': 'Cosas rarunas',
                'season_number': 1,
                'season_name': 'Temporada 1'
            },
            'review': 'This is a review',
            'rating': 5,
            'date': '2020-01-01'
        })
        assert isinstance(review, Review)

    def test_rating_exception(self):
        """Test that and exception is raised when the rating is not between 0 and 10."""
        with pytest.raises(ValueError):
            Review({
                'reviewer_id': '1',
                'season_info': {
                    'show_name': 'Cosas rarunas',
                    'season_number': 1,
                    'season_name': 'Temporada 1'
                },
                'review': 'This is a review',
                'rating': 11,
                'date': '2020-01-01'
            })
