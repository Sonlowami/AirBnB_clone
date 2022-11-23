#!/usr/bin/python3
"""
BaseModel Class Test
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.Testcase):
    """
    Test for BaseModel Class Methods
    """
    def test_str(self):
        """Test if ___str__ show the right output"""
        self.objct = BaseModel()
        self.string = f'[{self.objct.__class__.name}] ({self.obj.id}) {self.obj.__dict__}'
        self.assertEqual(self.string, str(self.objct))

    def test_save(self):
        """Test if updates are made when changes occur"""
        self.objct = BaseModel()
        self.assertNotEqual(self.objct.created_at, self.objct.updated_at)

    if __name__ == '__main__':
        unittest.main()
