#!/usr/bin/python3
"""Implements Unittests for Place class."""
import unittest
from ...models.place import Place


class TestPlace(unittest.TestCase):
    """Defines Unittests for Place class.

    Todo:
        * Test if instance attributes are initialized to correct values.
        * Test if id is always unique.
        * Test if save() method updates updated_at attribute correctly.
        * Test if string representation of instance, returned
            by __str__() is correct.
        * Test if dictionary representation of instance, returned by
            to_dict() is correct.
    """

    def setUp(self):
        self.Place_1 = Place()


if __name__ == '__main__':
    unittest.main()
