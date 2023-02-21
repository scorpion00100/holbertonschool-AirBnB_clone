#!/usr/bin/python3
"""module of User"""

from models.base_model import BaseModel


class User(BaseModel):
    """class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
