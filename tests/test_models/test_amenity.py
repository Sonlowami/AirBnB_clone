#!/usr/bin/python3i
"""
test of Amenity Class

"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ Test User Class """
    obj = Amenity()

    def test_attribute_name(self):
        """ Check name """
        self.assertEqual(hasattr(self.obj, "name"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.obj.name), str)

if __name__ == '__main__':
    unittest.main()
