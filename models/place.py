#!/usr/bin/python3
from models.base_model import BaseModel
from models.city import City
from models.user import User
"""
Class that represent a place
Inherits from BaseModel class
"""


class Place(BaseModel):
    """
    This class represents a place. It inherits from the BaseModel class,
    which provides basic attributes such as an id, creation and
    update timestamps, and serialization methods.

    Attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list - empty list

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
        """Constructor for Place class"""

        super().__init__(*args, **kwargs)
