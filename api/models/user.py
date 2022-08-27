"""This module is used for the user class."""


class User:
    """Class that represents an user of the appication."""

    def __init__(self, id: int, username: str, password: str, email: str, options: dict) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.options = options
