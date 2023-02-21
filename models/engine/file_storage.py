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
        """serializes __objects to the JSON file
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()"""
        
        my_dict = {k: v.to_dict(), for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w") as f:
            json.dumps(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass
