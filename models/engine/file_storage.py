#!/usr/bin/python3
"""module for FileStorage class"""

import json


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
        with open(FileStorage.__file_path, "w") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

