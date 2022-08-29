"""This module is used for the review class."""
from typing import Any


class ShowInfo:
    """Class that represents the show info in the review class."""

    def __init__(self, show_name: str, season_number: int, season_name: str) -> None:
        self.show_name = show_name
        self.season_number = season_number
        self.season_name = season_name


class Review:
    """Class that represents a review."""

    def __init__(self, reviewer: str, show_info: ShowInfo, review: str, rating: int) -> None:
        self.reviewer = reviewer
        self.show_info = show_info
        self.review = review
        self.rating = rating

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "rating" and (value < 0 or value > 10):
            raise ValueError("Rating must be between 0 and 10")
