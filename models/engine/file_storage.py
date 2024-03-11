#!/usr/bin/python3
"""FileStorage Class module"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """defines all common attributes/methods for other classes:

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        FileStorage.__objects
        ["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, mode="w") as f:
            dictt = {}
            for x, y in FileStorage.__objects.items():
                dictt[x] = y.to_dict()
            json.dump(dictt, f)

    def reload(self):
        """deserializes the JSON file to __objects if file exists."""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
