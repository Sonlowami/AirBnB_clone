#!/usr/bin/python3
"""
BaseModel Class Test
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel Class Methods
    """
    @classmethod
    def setup(cls):
        """set up an object for test"""
        cls.my_model = BaseModel()
        cls.my_model.name = "Holberton"
        cls.my_model.my_number = 89

    @classmethod
    def teardown(cls):
        """Delete the object at the end of test"""
        del cls.my_model

    def test_str(self):
        """Test if ___str__ show the right output"""
        string = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save(self):
        """Test if updates are made when changes occur"""
        self.assertNotEqual(self.objct.created_at, self.objct.updated_at)

    def test_to_dict(self):
        """"Test if updated_at and created_at changed their format
            Test if key __clas__ has a value BaseModel"""
        self.object_dict = self.object.to_dict()
        self.assertEqual(self.objct_dict['updated_at'], self.object.updated_at.isoformat())
        self.assertEqual(self.objct_dict['created_at'], self.object.created_at.isoformat())
        self.assertEqual(self.object.__class__.name, 'BaseModel')
if __name__ == '__main__':
    unittest.main()
