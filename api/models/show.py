"""This module is used for the shows model and its connection to TheMovieDB API."""
from typing import Tuple
import requests
import json
from datetime import date
from config.themoviedb_config import SHOWS_DB_API, SHOWS_DB_API_KEY, SHOWS_DB_LANGUAGE


class RequestException(Exception):
    """Class that represents a exception that can be raised when the request to the API fails."""

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


class Episode:
    """Class that represents a season episode"""

    def __init__(self, data: dict) -> None:
        """
        Constructor of the Episode class.
        Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - episode_number: int
            - name: str
            - overview: str
            - air_date: str in the format YYYY-MM-DD
            - still_path: str

        """
        self.number = int(data.get('episode_number'))
        self.name = str(data.get('name'))
        self.overview = str(data.get('overview'))
        self.air_date = date.fromisoformat(data.get('air_date'))
        self.thumbnail_path = str(data.get('still_path'))


class Season:
    """
    Class that represents a TV show season.
    Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - season_number: int
            - name: str
            - overview: str
            - air_date: str in the format YYYY-MM-DD
            - poster_path: str
            - episodes: list[Episode in JSON format]
    """

    def __init__(self, data: dict) -> None:
        self.season_number = int(data.get('season_number'))
        self.name = str(data.get('name'))
        self.overview = str(data.get('overview'))
        self.air_date = date.fromisoformat(data.get('air_date')) if data.get('air_date') else None
        self.poster_path = str(data.get('poster_path'))
        self.episodes = [Episode(episode) for episode in data.get('episodes', [])]


class Show:
    """
    Class that represents a TV show.
    Uses a JSON dictionary to initialize the attributes of the class.
        JSON dictionary must have the following keys:
            - id: int
            - name: str
            - genres: list[{id: int, name: str}]
            - overview: str
            - first_air_date: str in the format YYYY-MM-DD
            - in_production: bool
            - poster_path: str
            - seasons: list[Season in JSON format]
    """

    def __init__(self, data: json) -> None:
        self.id = int(data.get('id'))
        self.name = str(data.get('name'))
        self.genres = [genre.get('name') for genre in data.get('genres', [])]
        self.overview = str(data.get('overview'))
        self.first_air_date = date.fromisoformat(data.get('first_air_date')) if data.get('first_air_date') else None
        self.finished_airing = not bool(data.get('in_production'))
        self.poster_path = str(data.get('poster_path'))
        self.seasons = [Season(season) for season in data.get('seasons', [])]

    @classmethod
    def __get_url(self, uri: str) -> str:
        """Returns the URL to the API given an uri."""
        return f"{SHOWS_DB_API}{uri}?api_key={SHOWS_DB_API_KEY}&language={SHOWS_DB_LANGUAGE}"

    @classmethod
    def list_shows(cls, query: str = None) -> Tuple[list['Show'], int]:
        """
        Returns a list of TV shows filtered by the query.
        The shows only have the following attributes:
            - id: int
            - name: str
            - overview: str
            - first_air_date: date
            - poster_path: str
        :param query: The query to filter the shows.
        :type query: str
        :return: A list of TV shows.
        :rtype: list[Show]
        :return: The total number of results.
        :rtype: int
        """
        uri = '/search/tv'
        query = query or ''
        api_response = requests.get(f"{cls.__get_url(uri)}&query='{query}'")
        if api_response.status_code == 200:
            api_response = json.loads(api_response.text)
            return [Show(show) for show in api_response.get('results')], api_response.get('total_results')
        else:
            raise RequestException(api_response.status_code, json.loads(api_response.text).get('errors')[0])

    @classmethod
    def get_show(cls, id: int) -> 'Show':
        """
        Returns the details of TV show.
        The seasons of the show will have their episode lists empty.
        """
        uri = f"/tv/{id}"
        api_response = requests.get(cls.__get_url(uri))
        if api_response.status_code == 200:
            api_response = json.loads(api_response.text)
            return Show(api_response)
        else:
            raise RequestException(api_response.status_code, api_response.status_message)

    def get_season(self, season_number: int) -> Season:
        """Returns the details of the selected season."""
        uri = f"/tv/{self.id}/season/{season_number}"
        api_response = requests.get(self.__get_url(uri))
        if api_response.status_code == 200:
            api_response = json.loads(api_response.text)
            return Season(api_response)
        else:
            raise RequestException(api_response.status_code, api_response.status_message)
