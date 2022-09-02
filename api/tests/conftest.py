"""Mocks and tests fixtures"""

import json
import pytest
import requests


class MockResponse(object):
    """Mocks a requests.Response object"""

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = json.dumps(json_data)


@pytest.fixture()
def mock_list_shows_request(monkeypatch):
    def fake_request(uri):
        return MockResponse(
            json_data={
                "page": 1,
                "results": [
                    {
                        "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                        "id": 1399,
                        "overview": "Loren Ipsum",
                        "first_air_date": "1989-12-17",
                        "name": "The Simpsons"
                    },
                    {
                        "poster_path": "/a1MlbLBZWzqU5XaxvzCYKU1FJck.jpg",
                        "id": 1402,
                        "overview": "Loren Ipsum",
                        "first_air_date": "1999-03-28",
                        "name": "Futurama"
                    }
                ],
                "total_results": 2,
                "total_pages": 1
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)


@pytest.fixture()
def mock_get_show_request(monkeypatch):
    def fake_request(uri):
        return MockResponse(
            json_data={
                "first_air_date": "1989-12-17",
                "genres": [
                    {
                        "id": 10759,
                        "name": "Action"
                    }
                ],
                "id": 1399,
                "in_production": True,
                "name": "The Simpsons",
                "overview": "Loren Ipsum",
                "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                "seasons": [
                    {
                        "air_date": "2019-01-01",
                        "name": "Season 1",
                        "overview": "Lorem ipsum",
                        "poster_path": "/path/to/poster.jpg",
                        "season_number": 0
                    }
                ]
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)


@pytest.fixture()
def mock_get_season_request(monkeypatch):
    def fake_request(uri):
        return MockResponse(
            json_data={
                "air_date": "2019-01-01",
                "episodes": [
                    {
                        "air_date": "2019-01-01",
                        "episode_number": 1,
                        "name": "Episode 1",
                        "overview": "Lorem ipsum",
                        "still_path": "/path/to/still.jpg",
                    },
                    {
                        "air_date": "2019-01-08",
                        "episode_number": 2,
                        "name": "Episode 2",
                        "overview": "Lorem ipsum",
                        "still_path": "/path/to/still.jpg",
                    }
                ],
                "name": "Season 1",
                "overview": "Lorem ipsum",
                "poster_path": "/path/to/poster.jpg",
                "season_number": 0
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)
