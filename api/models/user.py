"""This module is used for the user class."""


class User:
    """Class that represents an user of the appication."""

    def __init__(self, username: str, password: str, email: str) -> None:
        self.username = username
        self.password = password
        self.email = email
