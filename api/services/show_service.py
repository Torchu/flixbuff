import json
from flask import Blueprint
from models.show import Show

blp = Blueprint('Show', __name__, url_prefix='/show')


@blp.route('/', methods=['GET'])
def get_shows():
    """Returns the list of shows divided by seasons"""
    return [show.to_json() for show in Show.get_show_list()]
