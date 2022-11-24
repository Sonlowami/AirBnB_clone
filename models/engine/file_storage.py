#!/usr/bib/python3
"""
File storage - create a class that saves to the a json file
and reads from it

"""
import json
import os.path
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
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            dic = {}
            for key, obj in FileStorage.__objects.items():
                dic[key] = obj.to_dict()
            json.dump(dic, f)

    def reload(self):
        """Deserialize a json object from a file into a dictionary"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                rd = f.read()
                if rd:
                    for key, obj in json.loads(rd).items():
                        if key == '__class__':
                            continue
                        FileStorage.__objects[key] = obj
