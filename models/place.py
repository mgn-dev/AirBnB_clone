#!/usr/bin/python3
"""This module is composed of Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines City class.

    Inherits from BaseModel.

    Attributes:
        city_id (str): holds the id of the city.
        user_id (str): holds the id of the user.
        name (str): holds the name of the city.
        description (str): holds description.
        number_rooms (int): holds number of rooms.
        number_bathrooms (int): holds number of bathrooms.
        max_guest (int): holds maximum number of guests.
        price_by_night (int): holds price per night.
        latitude (float): holds latitude coordinates.
        longitude (float): holds longitude coordinates.
        amenity_ids (list): holds a list of amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
