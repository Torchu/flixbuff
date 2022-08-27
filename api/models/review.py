"""This module is used for the review class."""
from typing import Any


class ReviewerInfo:
    """Class that represents the reviewer info in the review class."""

    def __init__(self, id: int, username: str) -> None:
        self.id = id
        self.username = username


class ShowInfo:
    """Class that represents the show info in the review class."""

    def __init__(self, show_id: int, show_name: str, season_id: int, season_name: str) -> None:
        self.show_id = show_id
        self.show_name = show_name
        self.season_id = season_id
        self.season_name = season_name


class Review:
    """Class that represents a review."""

    def __init__(self, id: int, reviewer: ReviewerInfo, show: ShowInfo, review: str, rating: int) -> None:
        self.id = id
        self.reviewer = reviewer
        self.show = show
        self.review = review
        self.rating = rating

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "rating" and (value < 0 or value > 10):
            raise ValueError("Rating must be between 0 and 10")
