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
                "results": [
                    {
                        "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                        "id": 1399,
                        "overview": "Loren Ipsum",
                        "name": "The Simpsons"
                    },
                    {
                        "post_path": "/a1MlbLBZWzqU5XaxvzCYKU1FJck.jpg",
                        "id": 1402,
                        "overview": "Loren Ipsum",
                        "name": "Futurama"
                    }
                ]
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)


@pytest.fixture()
def mock_get_show_request(monkeypatch):
    def fake_request(uri):
        return MockResponse(
            json_data={
                "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                "id": 1399,
                "overview": "Loren Ipsum",
                "name": "The Simpsons",
                "genres": [
                    {
                        "id": 10759,
                        "name": "Action"
                    }
                ],
                "seasons": [
                    {
                        "air_date": "2019-01-01",
                        "id": 1,
                        "name": "Season 1",
                        "overview": "Lorem ipsum",
                        "poster_path": "/path/to/poster.jpg",
                        "season_number": 1
                    }
                ]
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)
