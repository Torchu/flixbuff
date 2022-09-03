"""Module to define a custom JSON encoder."""
from flask.json import JSONEncoder
from bson import ObjectId
from typing import Any


class CustomJSONEncoder(JSONEncoder):
    """Class to define a custom JSON encoder."""

    def default(self, obj: Any) -> Any:
        """
        Default method to encode the object.
        :param obj: Object to encode
        :return: The encoded object
        """
        # If it's and ObjectId, returns the string representation
        if isinstance(obj, ObjectId):
            return str(obj)

        # If it's any other object, returns it as a dict
        elif isinstance(obj, object):
            return obj.__dict__

        # If it's any other type, returns the default encoding
        else:
            return JSONEncoder.default(self, obj)
