#!/usr/bin/python3
"""
Class that represent amenity
Inherits from BaseModel class
"""


class Amenity(BaseModel):
    """
    This class represents an amenity, such as Wi-Fi,
    a pool, or parking.
    It inherits from the BaseModel class, which provides
    basic attributes such as an id, creation and update timestamps,
    and serialization methods.

    Attributes:
        name (str): the name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity class"""

        super().__init__(*args, **kwargs)
