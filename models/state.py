#!/usr/bin/python3
from models.base_model import BaseModel
"""
Class that represent  a state.
Inherits from BaseModel class
"""


class State(BaseModel):
    """
    This class represents a state. It inherits from the BaseModel class,
    which provides basic attributes such as an id, creation and
    update timestamps, and serialization methods.

    Attributes:
        id (str): unique identifier of the state.
        created_at (datetime): creation timestamp in UTC format.
        updated_at (datetime): update timestamp in UTC format.
        name (str): the name of the state.

    Methods:
        __init__(self, *args, **kwargs):
            Constructor method for the State class. It calls the super()
            method to initialize the BaseModel attributes.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for State class"""

        super().__init__(*args, **kwargs)
