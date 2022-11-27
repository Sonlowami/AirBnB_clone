#!/usr/bin/python3
"""
Parent class BaseModel

This class contain the basic methods and attributes that
other model classes will extend.

"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Class containing key methods and attributes to be extended
    by all model classes
    """
    def __init__(self, *args, **kwargs):
        """Create instance attribue"""
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Make a change to an object and update it"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all attributes of a BaseModel object
        """
        copy = dict(vars(self))
        copy['created_at'] = copy['created_at'].isoformat()
        copy['updated_at'] = copy['updated_at'].isoformat()
        copy["__class__"] = self.__class__.__name__
        return copy
