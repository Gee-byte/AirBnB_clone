#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represnt  a user.
    Inherits from BaseModel class

    Attributes:
        id (str): A unique identifier for the user.
        created_at (datetime): The date and time the user was created.
        updated_at (datetime): The date and time the user was last updated.
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    Methods:
        __init__: Initializes a new instance of the 'User' class.
        __str__: Returns a string representation of the 'User'
                        in the format '[<class name>] (<id>) <__dict__>.'
        save: Updates the public instance attribute 'updated_at' with the
        current datetime.
        to_dict: Returns a dictionary containing all keys and values of the
                '__dict__' of the instance.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for User class"""
        super().__init__(*args, **kwargs)
