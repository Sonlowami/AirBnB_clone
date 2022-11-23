#!/usr/bin/python3
"""
Parent class BaseModel

This class contain the basic methods and attributes that
other model classes will extend.

"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Class containing key methods and attributes to be extended
    by all model classes
    """
    def __init__(self):
        """Create instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.__dict__["__class__"] = self.__class__.__name__

    def __str__(self):
        """Return a string representation of the BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Make a change to an object and update it"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all attributes of a BaseModel object
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return vars(self)
