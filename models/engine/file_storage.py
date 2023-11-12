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
        # with open(self.__file_path, mode='w') as store_file:
        #     json.dump(self.__objects, store_file)
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        # try:
        #     with open(self.__file_path, mode='r') as retrieval_file:
        #         if os.path.getsize(self.__file_path) > 0:
        #             self.__objects = json.load(retrieval_file)
        # except FileNotFoundError:
        #     pass
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
