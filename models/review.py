#!/usr/bin/python3
"""module for class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class for managing Review objects"""
    place_id = ""
    user_id = ""
    text = ""
