from flask import Blueprint
from models.show import Show

blp = Blueprint('Show', __name__, url_prefix='/show')


@blp.route('/', methods=['GET'])
def list_shows() -> dict:
    """Returns the list of shows"""
    return [show.to_json() for show in Show.list_shows()]


@blp.route('/<int:id>', methods=['GET'])
def get_show(id: int) -> dict:
    """Returns the details of a shows"""
    return Show.get_show(id).to_json()
