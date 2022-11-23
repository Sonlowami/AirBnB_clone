#!/usr/bib/python3

"""
File storage - create a class that saves to the a json file
and reads from it

"""
from models.base_model import BaseModel


class FileStorage:
    """Create a file storage class"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return all objects created and saved"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the object dictionary"""
            if not isinstance(obj, BaseModel):
                return
            FileStorage.__objects["{self.__class__.__name__}.{self.id}"] = obj

    def save(self):
        """Serialize objects to json file"""
        try:
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                json.dump(FileStorage.__objects, f)
        except FileNotFoundError:
            return

    def reload(self):
        """Deserialize a json object from a file into a dictionary"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            return
