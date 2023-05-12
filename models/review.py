#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
Class that represent review
Inherits from BaseModel class
"""


class Review(BaseModel):
    """
    The Review class is a model that represents a review.
    It inherits from the 'BaseModel' class, which provides
    basic attributes such as an 'id', creation and update
    timestamps, and serialization methods.

    Attributes:
        place_id (str): empty string; it will be the 'Place.id'
        user_id (str): empty string; it will be the 'User.id'
        text (str): empty string

    """
    place_id = Place.id
    user_id = User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Review class"""

        super().__init__(*args, **kwargs)
