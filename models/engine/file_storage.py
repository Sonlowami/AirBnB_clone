#!/usr/bib/python3

"""
File storage - contains file storage class

"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Store the objects to a file for persistance"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Add object to the array of objects"""
        if obj not isinstance(obj, BaseModel):
                return
        FileStorage.__objects["{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize the __objects into a json"""
        try:
            with open(__file_path, 'w', encoding="utf-78") as f:
                json.dump(__objects, __file_path)
        except:
            return

    def reload(self):
        """Deserialize the json file"""
        try:
            with open(__file_path) as f:
                FileStorage.__objects = json.load(f)
        except:
            return

