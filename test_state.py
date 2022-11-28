#!/usr/bin/python3
"""Test of State Class """

from models.state import State
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ Test User Class """
    model = State()

    def test_attribute(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.model, "name"), True)

    def test_types(self):
        """ test types"""
        self.assertEqual(type(self.model.name), str)

if __name__ == '__main__':
    unittest.main()
