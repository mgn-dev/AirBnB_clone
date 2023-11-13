#!/usr/bin/python3
"""This module comprises of Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines Amenity class

    Inherits from BaseModel

    Attributes:
        name (str): holds the name of amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
