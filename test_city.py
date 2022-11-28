#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Test City Class """
    obj = City()

    def test_attribute(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.obj, "state_id"), True)
        self.assertEqual(hasattr(self.obj, "name"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.obj.state_id), str)
        self.assertEqual(type(self.obj.name), str)

if __name__ == '__main__':
    unittest.main()
