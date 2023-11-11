#!/usr/bin/python3
"""Implements Unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines Unittests for BaseModel class.

    Todo:
        * Test if instance attributes are initialized to correct values.
        * Test if id is always unique.
        * Test if save() method updates updated_at attribute correctly.
        * Test if string representation of instance, returned
            by __str__() is correct.
        * Test if dictionary representation of instance, returned by
            to_dict() is correct.
    """

    def test_BaseModel_init(self):
        pass


if __name__ == '__main__':
    unittest.main()
