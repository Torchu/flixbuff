"""This module is used for the shows model."""
from datetime import date


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
