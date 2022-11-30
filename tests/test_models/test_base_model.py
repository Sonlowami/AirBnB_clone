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
    def setUp(self):
        """set up an object for test"""
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89

        self.objct = BaseModel()
        self.objct.name = "Keriane"
        self.objct.my_number = 2022

    @classmethod
    def tearDown(self):
        """Delete the object at the end of test"""
        del self.my_model

    def test_str(self):
        """Test if ___str__ show the right output"""
        string = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save(self):
        """Test if updates are made when changes occur"""
        self.objct.save()
        self.assertNotEqual(self.objct.created_at, self.objct.updated_at)

    def test_to_dict(self):
        """"Test if updated_at and created_at changed their format
            Test if key __clas__ has a value BaseModel"""
        objct_dict = self.objct.to_dict()
        self.assertEqual(objct_dict['updated_at'], self.objct.updated_at.isoformat())
        self.assertEqual(objct_dict['created_at'], self.objct.created_at.isoformat())
        self.assertEqual(self.objct.__class__.__name__, 'BaseModel')
if __name__ == '__main__':
    unittest.main()
