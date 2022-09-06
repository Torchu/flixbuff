"""This module is used for the review class."""
from typing import Any, Dict, List, Union, Tuple
from flask import current_app
import pymongo
from models.show import Show


class SeasonNotFoundError(Exception):
    """Class that represents a exception that can be raised when the season is not found."""

    def __init__(self) -> None:
        self.code = 400
        self.message = 'Season not found'


class SeasonInfo:
    """Class that represents the season info in the review class."""

    def __init__(self, data: Dict) -> None:
        """
        Constructor of the SeasonInfo class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - show_id: int
            - show_name: str
            - season_number: int
            - season_name: str
        """
        self.show_id = data.get('show_id')
        self.show_name = data.get('show_name')
        self.season_number = data.get('season_number')
        self.season_name = data.get('season_name')


class Review:
    """Class that represents a review."""

    def __init__(self, data: Dict) -> None:
        """
        Constructor of the Review class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - _id: str
            - reviewer_id: str
            - season_info: dict {show_name: str, season_number: int, season_name: str}
            - review: str
            - rating: int

        """
        self._id = data.get('_id')
        self.reviewer = data.get('reviewer_id')
        self.season_info = SeasonInfo(data.get('season_info', {}))
        self.review = data.get('review')
        self.rating = data.get('rating')

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "rating" and value is not None and (value < 0 or value > 5):
            raise ValueError("Rating must be between 0 and 5")
        super().__setattr__(key, value)

    def to_json(self) -> Dict:
        """Returns the review object as a JSON."""
        return {
            "_id": str(self._id),
            "reviewer_id": self.reviewer,
            "season_info": self.season_info.__dict__,
            "review": self.review,
            "rating": self.rating
        }

    def complete_season_info(self) -> None:
        """Completes the season info with the name of the show and the season."""
        show = Show.get_show(self.season_info.show_id)  # If this fails, it will raise a RequestException
        self.season_info.show_name = show.name
        season = next((season for season in show.seasons if season.season_number ==
                      self.season_info.season_number), None)
        if season is not None:
            self.season_info.season_name = season.name
        else:
            raise SeasonNotFoundError

    def insert(self) -> 'Review':
        """
        Inserts the review into the database.
        :return: Review object
        """
        # Maps the review object to a dictionary
        data_to_insert = self.to_json()

        # Erases the ID if it exists
        if '_id' in data_to_insert:
            del data_to_insert['_id']

        # Inserts the review into the database
        review_id = current_app.mongo.db.reviews.insert_one(data_to_insert).inserted_id

        # Returns the review object
        return Review.find({'_id': review_id})

    @classmethod
    def find(cls, criteria: Dict) -> Union['Review', None]:
        """
        Finds a review in the database.
        :param criteria: Dictionary with the search criteria
        :return: Review object
        """
        review_data = current_app.mongo.db.reviews.find_one(criteria)
        review_item = Review(review_data) if review_data else None
        return review_item

    @classmethod
    def list_from_user(cls, user_id: str) -> Tuple[List['Review'], int]:
        """
        Returns the list of reviews from the given user
        :param user_id: User ID
        :return: List of reviews
        """
        cursor = current_app.mongo.db.reviews.find({'reviewer_id': user_id})
        cursor.sort('_id', pymongo.DESCENDING)
        reviews = [Review(review) for review in cursor]
        total = current_app.mongo.db.reviews.count_documents({'reviewer_id': user_id})
        return reviews, total

    @classmethod
    def list(cls) -> Tuple[List['Review'], int]:
        """
        Returns the list of reviews
        :return: List of reviews
        """
        cursor = current_app.mongo.db.reviews.find()
        cursor.sort('_id', pymongo.DESCENDING)
        reviews = [Review(review) for review in cursor]
        total = current_app.mongo.db.reviews.count_documents({})
        return reviews, total

    @classmethod
    def list_from_user_list(cls, users: List[str]) -> Tuple[List['Review'], int]:
        """
        Returns the list of reviews from the given users
        :param users: list of users IDs
        :return: List of reviews
        """
        cursor = current_app.mongo.db.reviews.find({'reviewer_id': {'$in': users}})
        cursor.sort('_id', pymongo.DESCENDING)
        reviews = [Review(review) for review in cursor]
        total = current_app.mongo.db.reviews.count_documents({'reviewer_id': {'$in': users}})
        return reviews, total
