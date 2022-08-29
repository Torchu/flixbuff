"""This module is used for the review class."""
from typing import Any


class SeasonInfo:
    """Class that represents the season info in the review class."""

    def __init__(self, show_name: str, season_number: int, season_name: str) -> None:
        self.show_name = show_name
        self.season_number = season_number
        self.season_name = season_name


class Review:
    """Class that represents a review."""

    def __init__(self, reviewer: str, season_info: SeasonInfo, review: str, rating: int) -> None:
        self.reviewer = reviewer
        self.season_info = season_info
        self.review = review
        self.rating = rating

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "rating" and (value < 0 or value > 10):
            raise ValueError("Rating must be between 0 and 10")
