#!/usr/bin/python3
"""This module is composed of Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review class.

    Inherits from BaseModel.

    Attributes:
        place_id (str): holds id of place.
        user_id (str): hold user id.
        text (str): hold user review.
    """

    place_id = ""
    user_id = ""
    text = ""
