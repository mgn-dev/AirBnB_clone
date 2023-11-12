#!/usr/bin/python3
"""This module is composed of User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user.

    Inherits from BaseModel.

    Attributes:
        email (str): represents user email.
        password (str): represents user password.
        first_name (str): represents user first name.
        last_name (str): represents user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
