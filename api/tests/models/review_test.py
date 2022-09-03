"""Test module for the Review model."""
import pytest
from datetime import date
from models.review import Review


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
            'rating': 5
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
                'rating': 11
            })

    def test_insert(self):
        """Test for the insert method."""
        review = Review({
            'reviewer_id': '1',
            'season_info': {
                'show_name': 'Cosas rarunas',
                'season_number': 1,
                'season_name': 'Temporada 1'
            },
            'review': 'This is a review',
            'rating': 5
        })
        assert review.insert() is not None, 'The review was not inserted'

    def test_find(self):
        """Test for the find method."""
        review = Review({
            'reviewer_id': '1',
            'season_info': {
                'show_name': 'Cosas rarunas',
                'season_number': 1,
                'season_name': 'Temporada 1'
            },
            'review': 'This is a review',
            'rating': 5
        })
        review.insert()

        assert Review.find({'reviewer_id': '1'}) is not None, 'The review was not found'
        assert Review.find({'reviewer_id': '2'}) is None, 'Unexisting review was found'
