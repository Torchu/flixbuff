from flask_rest_api import Blueprint
from schemas.show_schema import ShowDetailsSchema, ShowListSchema
from models.show import Show

blp = Blueprint('Show', 'Show', url_prefix='/show')


@blp.route('', methods=['GET'])
@blp.response(ShowListSchema, code=200)
def list_shows() -> dict:
    """Returns the list of shows"""
    return {
        "items": [show for show in Show.list_shows()],
        "total": len(Show.list_shows())
    }


@blp.route('/<int:id>', methods=['GET'])
@blp.response(ShowDetailsSchema, code=200)
def get_show(id: int) -> dict:
    """Returns the details of a shows"""
    return Show.get_show(id)
