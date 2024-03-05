#!/usr/bin/python3
"""FileStorage Class module"""
import json
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
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        dictt = self.__objects
        object_dict = {obj: dictt[obj].to_dict() for obj in dictt.keys()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(object_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects if file exists."""
        try:
            with open(self.__file_path) as json_file:
                loaded_objects = json.load(json_file)
                for key in loaded_objects.values():
                    class_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(class_name) (**key))
        except FileNotFoundError:
            return
