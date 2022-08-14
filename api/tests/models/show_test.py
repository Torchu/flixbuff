"""Test module for the Show model."""
from models.show import Season
from models.show import Show


class TestSeason():
    """Test class for the Season model."""

    def test_from_json(self):
        """Tests the from_json method of the Season class."""
        json_data = {
            'air_date': '2019-01-01',
            'id': 1,
            'name': 'Season 1',
            'overview': 'Lorem ipsum',
            'poster_path': '/path/to/poster.jpg',
            'season_number': 1
        }
        season = Season.from_json(json_data)
        assert season.air_date == '2019-01-01'
        assert season.id == 1
        assert season.name == 'Season 1'
        assert season.overview == 'Lorem ipsum'
        assert season.poster_path == '/path/to/poster.jpg'
        assert season.season_number == 1

    def test_to_json(self):
        """Tests the to_json method of the Season class."""
        season = Season('2019-01-01', 1, 'Season 1',
                        'Lorem ipsum', '/path/to/poster.jpg', 1)
        assert season.to_json() == {
            'air_date': '2019-01-01',
            'id': 1,
            'name': 'Season 1',
            'overview': 'Lorem ipsum',
            'poster_path': '/path/to/poster.jpg',
            'season_number': 1
        }


class TestShow():
    """Test class for the Show model."""

    def test_from_json(self):
        """Tests the from_json method."""
        show = Show.from_json({
            "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
            "id": 1399,
            "overview": "Loren Ipsum",
            "name": "The Simpsons",
            "genres": [{"id": 10759, "name": "Action"}],
            "seasons": [{
                "air_date": "2019-01-01",
                "id": 1,
                "name": "Season 1",
                "overview": "Lorem ipsum",
                "poster_path": "/path/to/poster.jpg",
                "season_number": 1
            }]
        })
        assert show.id == 1399
        assert show.name == "The Simpsons"
        assert show.genres == ["Action"]
        assert show.overview == "Loren Ipsum"
        assert show.poster_path == "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg"
        assert show.seasons[0].name == "Season 1"

    def test_list_shows(self, mock_list_shows_request):
        """Tests the list_shows method."""
        assert [show.name for show in Show.list_shows()] == [
            "The Simpsons", "Futurama"]

    def test_to_json(self):
        """Tests the to_json method."""
        show = Show(1399,
                    "The Simpsons",
                    ['action'],
                    "Loren Ipsum",
                    "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                    [Season("19-02-2012", 1, "Season 1", "Loren Ipsum",
                            "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg", 1)]
                    )
        assert show.to_json() == {
            "id": 1399,
            "name": "The Simpsons",
            "genres": ['action'],
            "overview": "Loren Ipsum",
            "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
            "seasons": [{
                "air_date": "19-02-2012",
                "id": 1,
                "name": "Season 1",
                "overview": "Loren Ipsum",
                "poster_path": "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg",
                "season_number": 1
            }]
        }

    def test_get_show(self, mock_get_show_request):
        """Tests the get_show method."""
        show = Show.get_show(1399)
        assert show.id == 1399
        assert show.name == "The Simpsons"
        assert show.genres == ["Action"]
        assert show.overview == "Loren Ipsum"
        assert show.poster_path == "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg"
        assert show.seasons[0].name == "Season 1"
