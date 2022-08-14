"""This module is used for the shows model and its connection to TheMovieDB API."""
import requests
import json
from datetime import date
from config.general_config import SHOWS_DB_API, SHOWS_DB_API_KEY, SHOWS_DB_LANGUAGE


class RequestException(Exception):
    """Class that represents a exception that can be raised when the request to the API fails."""

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


class Season:
    """Class that represents a TV show season."""

    def __init__(
        self,
        season_number: int,
        name: str,
        overview: str,
        air_date: str,
        number_of_episodes: int,
        poster_path: str
    ) -> None:
        self.name = name
        self.overview = overview
        self.air_date = air_date
        self.poster_path = poster_path
        self.number_of_episodes = number_of_episodes
        self.season_number = season_number

    @classmethod
    def from_json(cls, json_data: dict) -> 'Season':
        """Creates a Season object from a json dict."""
        return cls(
            air_date=json_data.get('air_date'),
            id=json_data.get('id'),
            name=json_data.get('name'),
            overview=json_data.get('overview'),
            poster_path=json_data.get('poster_path'),
            season_number=json_data.get('season_number')
        )

    def to_json(self) -> dict:
        """Returns a json dict with the season data."""
        return self.__dict__


class Show:
    """Class that represents a TV show."""

    def __init__(
        self,
        name: str,
        genres: list[str],
        overview: str,
        first_air_date: date,
        finished_airing: bool,
        poster_path: str,
        seasons: list[Season]
    ) -> None:
        self.name = name
        self.genres = genres
        self.overview = overview
        self.first_air_date = first_air_date
        self.finished_airing = finished_airing
        self.poster_path = poster_path
        self.seasons = seasons

    @classmethod
    def __get_url(self, uri: str) -> str:
        """Returns the URL to the API given an uri."""
        return f"{SHOWS_DB_API}{uri}?api_key={SHOWS_DB_API_KEY}&language={SHOWS_DB_LANGUAGE}"

    @classmethod
    def from_json(cls, json_data: dict) -> 'Show':
        """Returns a Show object from a JSON representation."""
        return cls(
            id=json_data.get('id'),
            name=json_data.get('name'),
            genres=[genre.get('name')
                    for genre in json_data.get('genres', [])],
            overview=json_data.get('overview'),
            poster_path=json_data.get('poster_path'),
            seasons=[Season.from_json(season)
                     for season in json_data.get('seasons', [])]
        )

    @classmethod
    def list_shows(cls) -> list['Show']:
        """Returns a list of TV shows."""
        uri = '/popular'
        api_response = requests.get(cls.__get_url(uri))
        if api_response.status_code == 200:
            api_response = json.loads(api_response.text)
            return [Show.from_json(show) for show in api_response.get('results')]
        else:
            raise RequestException(
                api_response.status_code, api_response.status_message)

    @classmethod
    def get_show(cls, id: int) -> 'Show':
        """Returns the details of TV show."""
        uri = f"/{id}"
        api_response = requests.get(cls.__get_url(uri))
        if api_response.status_code == 200:
            api_response = json.loads(api_response.text)
            return Show.from_json(api_response)
        else:
            raise RequestException(
                api_response.status_code, api_response.status_message)

    def to_json(self) -> dict:
        """Returns a JSON representation of the show."""
        json = self.__dict__
        json['seasons'] = [season.to_json() for season in self.seasons]
        return json
