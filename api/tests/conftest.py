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
def mock_get_show_list_request(monkeypatch):
    def fake_request(uri):
        return MockResponse(
            json_data={
                "results": [
                    {
                        "name": "The Simpsons"
                    },
                    {
                        "name": "Futurama"
                    }
                ]
            },
            status_code=200
        )
    monkeypatch.setattr(requests, 'get', fake_request)
