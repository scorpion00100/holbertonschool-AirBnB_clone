#!/usr/bin/python3
"""module for City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """class that inherits from BaseModel"""
    state_id = ""
    name = ""
