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
            if os.path.getsize(self.__file_path) != 0:
                with open(self.__file_path) as json_file:
                    loaded_objects = json.load(json_file)
                    for key in loaded_objects.values():
                        class_name = key.pop("__class__", None)
                        if class_name:
                            obj = eval(class_name)(**key)
                            self.new(obj)
            else:
                return
        except FileNotFoundError:
           print(f"Error: the file '{self.__file_path}' does not exist")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{self.__file_path}': {e}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
