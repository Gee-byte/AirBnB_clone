#!/usr/bin/python3
"""Defines a base model class."""
from datetime import datetime
from models import storage
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Represent the "base" for all other classes in the AirBnB clone
    project.
    Attributes:
        id: string,assigned a unique 'uuid'when an instance is created.
            Use 'uuid.uuid4()' to generate a unique 'uuid'.
        created_at: 'datetime' object,assigned the current datetime when
                    an instance is created.
        updated_at: 'datetime' object, assigned the current datetime when an
                    instance is created, and updated every time the object is
                    changed.
    Methods:
        __init__: Initializesa new instance of the
                                        'BaseModel' class.
        __str__: Returns a string representation of the 'BaselModel'
                        in the format '[<class name>] (<id>) <__dict__>.'
        save: Updates the public instance attribute 'updated_at' with the
        current datetime.
        to_dict: Returns a dictionary containing all keys and values of the
                '__dict__' of the instance.
    """

    def __init__(self, *args, **kwargs):
        """initialization Base
        *args won’t be used
        if kwargs is not empty:
        each key of this dictionary is an attribute name
        each value of this dictionary is the value of this attribute name
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                if key in ['created_at', 'updated_at']:
                    setattr(self, key, self.string2time(value))
                    continue

                setattr(self, key, value)

        else:
            uuid_gen = uuid.uuid4()
            self.id = str(uuid_gen)
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

            models.storage.new(self)

    @staticmethod
    def string2time(date_string):
        """Converts string to time"""
        return datetime.strptime(date_string, time)

    def __str__(self):
        """Returns string representation of an instance"""
        return("[{}] ({}) {}"
               .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Save an instance and set the updated time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the attributes of the instance as a dict"""
        var = self.__dict__.copy()

        var['__class__'] = self.__class__.__name__
        var['created_at'] = self.created_at.isoformat()
        var['updated_at'] = self.updated_at.isoformat()
        return var
