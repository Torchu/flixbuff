from flask_rest_api import Blueprint, abort
from schemas.show_schema import ShowDetailsSchema, ShowListSchema, SeasonSchema
from models.show import Show, RequestException

blp = Blueprint('Show', 'Show', url_prefix='/show')


@blp.route('', methods=['GET'])
@blp.response(ShowListSchema, code=200)
def list_shows() -> dict:
    """Returns the list of shows"""
    try:
        return {
            "items": [show for show in Show.list_shows()],
            "total": len(Show.list_shows())
        }
    except RequestException as e:
        abort(e.code, message=e.message)


@blp.route('/<int:id>', methods=['GET'])
@blp.response(ShowDetailsSchema, code=200)
def get_show(id: int) -> dict:
    """Returns the details of a shows"""
    try:
        return Show.get_show(id)
    except RequestException as e:
        abort(e.code, message=e.message)


@blp.route('/<int:id>/season/<int:season_number>', methods=['GET'])
@blp.response(SeasonSchema, code=200)
def get_show(id: int, season_number: int) -> dict:
    """Returns the details of the season"""
    try:
        show = Show.get_show(id)
        return show.get_season(season_number)
    except RequestException as e:
        abort(e.code, message=e.message)
