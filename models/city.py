#!/usr/bin/python3
"""This module is composed of City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines City class.

    Inherits from BaseModel.

    Attributes:
        state_id (str): holds the id of the state.
        name (str): holds the name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
