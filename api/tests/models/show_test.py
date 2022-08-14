"""Test module for the Show model."""
from models.show import Show


class TestShow():
    """Test class for the Show model."""

    def test_get_show_list(self, mock_get_show_list_request):
        """Tests the get_show_list method."""
        assert [show.name for show in Show.get_show_list()] == [
            "The Simpsons", "Futurama"]

    def test_to_json(self):
        """Tests the to_json method."""
        show = Show("The Simpsons")
        assert show.to_json() == {"name": "The Simpsons"}
