#!/usr/bin/python3
"""This module implements BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (string): uuid when an instance is created.
        created_at (datetime): current datetime when an instance is created.
        updated_at (datetime): current datetime when an instance is created
            and it will be updated every time you change your object.

    Args
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(val))
                else:
                    setattr(self, key, val)

    def __str__(self):
        """Overwrites the string representation of this method's class."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Defines a dictionary representation of this object.

        Returns:
            a dictionary containing all
            keys/values of __dict__ of the instance.
        """
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()

        for key, val in self.__dict__.items():
            if key not in ['created_at', 'updated_at', '__class__']:
                new_dict[key] = val

        return new_dict
