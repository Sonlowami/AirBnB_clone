#!usr/bin/python3

"""

Ïnherites from Basemodel
"""
from models.base_model import basemodel

class user(BaseModel):
    """

    Class user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
