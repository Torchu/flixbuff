"""This module is used for the review class."""
from typing import Any
from datetime import date


class SeasonInfo:
    """Class that represents the season info in the review class."""

    def __init__(self, data: dict) -> None:
        """
        Constructor of the SeasonInfo class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - show_name: str
            - season_number: int
            - season_name: str
        """
        self.show_name = data.get('show_name')
        self.season_number = data.get('season_number')
        self.season_name = data.get('season_name')


class Review:
    """Class that represents a review."""

    def __init__(self, data: dict) -> None:
        """
        Constructor of the Review class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - _id: str
            - reviewer_id: str
            - season_info: dict {show_name: str, season_number: int, season_name: str}
            - review: str
            - rating: int
            - date: date in the format YYYY-MM-DD

        """
        self._id = data.get('_id')
        self.reviewer = data.get('reviewer_id')
        self.season_info = SeasonInfo(data.get('season_info', {}))
        self.review = data.get('review')
        self.rating = data.get('rating')
        self.date = date.fromisoformat(data.get('date'))

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "rating" and (value < 0 or value > 10):
            raise ValueError("Rating must be between 0 and 10")
