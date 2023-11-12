#!/usr/bin/python3
"""This module implements FileStorage class."""
import json
import os


class FileStorage:
    """Deals with serialization of instances to and from a JSON file.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): empty but will store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (object): class instance
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file."""
        if self.__objects:
            with open(self.__file_path, mode='w') as store_file:
                json.dump(self.__objects, store_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, mode='r') as retrieval_file:
                if os.path.getsize(self.__file_path) > 0:
                    self.__objects = json.load(retrieval_file)
        except FileNotFoundError:
            pass
