#!/usr/bin/python3
"""Implements Unittests for State class."""
import unittest
from ...models.state import State


class TestState(unittest.TestCase):
    """Defines Unittests for State class.

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
        self.State_1 = State()


if __name__ == '__main__':
    unittest.main()
