from flask_rest_api import Blueprint
from models.test import Test

blp = Blueprint('Test', 'Test', url_prefix='/test')


@blp.route('', methods=['GET'])
@blp.response(code=200)
def greet() -> str:
    """Greets"""
    test = Test()
    return test.greet()


@blp.route('/<string:name>', methods=['GET'])
@blp.response(code=200)
def greet_person(name: str) -> str:
    """Greets the person"""
    test = Test()
    return test.personal_greeting(name)
