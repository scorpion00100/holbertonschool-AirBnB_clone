#!/usr/bin/python3
"""module for FileStorage class"""

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
    """class that serializes and deserializes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        di_ctio = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                   for key, value in obj_dict.items():
                    self.new(di_ctio[value['__class__']](**value))
            return
