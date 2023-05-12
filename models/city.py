#!/usr/bin/python3
from models.state import State
"""
Class that represent  a city.
Inherits from BaseModel class
"""


class City(BaseModel):
    """
    This class represents a city. It inherits from the BaseModel class,
    which provides basic attributes such as an id, creation and
    update timestamps, and serialization methods.

    Attributes:
        state_id (str): The id of the state this city belongs to.
        name (str): The name of the city.
    """
    state_id = State.id
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for City class"""

        super().__init__(*args, **kwargs)
