from flask_rest_api import Blueprint, abort
from schemas.shared_schemas import QueryParametersSchema
from schemas.show_schema import ShowDetailsSchema, ShowListSchema, SeasonSchema
from models.show import Show, RequestException

blp = Blueprint('Show', 'Show', url_prefix='/show')


@blp.route('', methods=['GET'])
@blp.arguments(QueryParametersSchema, location='query')
@blp.response(ShowListSchema, code=200)
def list_shows(params: dict) -> dict:
    """Returns the list of shows"""
    try:
        show_list, total = Show.list_shows(params.get('query'))
        return {
            "items": [show for show in show_list],
            "total": total
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
