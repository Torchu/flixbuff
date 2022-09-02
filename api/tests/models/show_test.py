"""Test module for the Show model."""
from datetime import date
from models.show import Show


class TestShow():
    """Test class for the Show model."""

    def test_list_shows(self, mock_list_shows_request):
        """Tests the list_shows method."""
        show_list = Show.list_shows()
        assert len(show_list) == 2, "The number of shows does not match."
        assert show_list[0].id == 1399, "The show id does not match."
        assert show_list[0].name == 'The Simpsons', "The show name does not match."
        assert show_list[0].overview == 'Loren Ipsum', "The show overview does not match."
        assert show_list[0].first_air_date == date(1989, 12, 17), "The show first air date does not match."
        assert show_list[0].poster_path == '/eKACS8xQjvkGz2QEkE80fPmO0y.jpg', "The show poster path does not match."
        assert show_list[1].id == 1402, "The show id does not match."
        assert show_list[1].name == 'Futurama', "The show name does not match."
        assert show_list[1].overview == 'Loren Ipsum', "The show overview does not match."
        assert show_list[1].first_air_date == date(1999, 3, 28), "The show first air date does not match."
        assert show_list[1].poster_path == '/a1MlbLBZWzqU5XaxvzCYKU1FJck.jpg', "The show poster path does not match."

    def test_get_show(self, mock_get_show_request):
        """Tests the get_show method."""
        show = Show.get_show(1399)
        assert show.id == 1399, "The show id does not match."
        assert show.name == "The Simpsons", "The show name does not match."
        assert show.genres == ["Action"], "The show genres does not match."
        assert show.overview == "Loren Ipsum", "The show overview does not match."
        assert show.first_air_date == date(1989, 12, 17), "The show first air date does not match."
        assert show.finished_airing == False, "The show finished airing does not match."
        assert show.poster_path == "/eKACS8xQjvkGz2QEkE80fPmO0y.jpg", "The show poster path does not match."
        assert len(show.seasons) == 1, "The number of seasons does not match."
        assert show.seasons[0].season_number == 0, "The season number does not match."
        assert show.seasons[0].name == "Season 1", "The season name does not match."
        assert show.seasons[0].overview == "Lorem ipsum", "The season overview does not match."
        assert show.seasons[0].air_date == date(2019, 1, 1), "The season air date does not match."
        assert show.seasons[0].poster_path == "/path/to/poster.jpg", "The season poster path does not match."

    def test_get_season(self, mock_get_season_request):
        """Tests the get_season method"""
        show = Show({
            "id": 1399
        })
        season = show.get_season(0)
        assert season.season_number == 0, "The season number does not match."
        assert season.name == "Season 1", "The season name does not match."
        assert season.overview == "Lorem ipsum", "The season overview does not match."
        assert season.air_date == date(2019, 1, 1), "The season air date does not match."
        assert season.poster_path == "/path/to/poster.jpg", "The season poster path does not match."
        assert len(season.episodes) == 2, "The number of episodes does not match."
        assert season.episodes[0].number == 1, "The episode number does not match."
        assert season.episodes[0].name == "Episode 1", "The episode name does not match."
        assert season.episodes[0].overview == "Lorem ipsum", "The episode overview does not match."
        assert season.episodes[0].air_date == date(2019, 1, 1), "The episode air date does not match."
        assert season.episodes[0].thumbnail_path == "/path/to/still.jpg", "The episode thumbnail path does not match."
        assert season.episodes[1].number == 2, "The episode number does not match."
        assert season.episodes[1].name == "Episode 2", "The episode name does not match."
        assert season.episodes[1].overview == "Lorem ipsum", "The episode overview does not match."
        assert season.episodes[1].air_date == date(2019, 1, 8), "The episode air date does not match."
        assert season.episodes[1].thumbnail_path == "/path/to/still.jpg", "The episode thumbnail path does not match."
