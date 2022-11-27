#!/usr/bib/python3
"""
File storage - create a class that saves to the a json file
and reads from it

"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Create a file storage class"""

    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel" : BaseModel, "User" : User, "State" : State, "City" : City, "Amenity" : Amenity, "Place" : Place, "Review" : Review}
    def all(self):
        """Return all objects created and saved"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the object dictionary"""
        if not isinstance(obj, BaseModel):
            return
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize objects to json file"""
        dic = {}
        for key, obj in self.__objects.items():
            dic[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """Deserialize a json object from a file into a dictionary"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                rd = f.read()
                if rd:
                    for key, obj in json.loads(rd).items():
                        objec = self.classes[obj['__class__']]
                        self.__objects[key] = objec(**obj)
