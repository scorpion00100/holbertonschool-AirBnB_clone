#!/usr/bin/python3
"""Test City"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testcity(unittest.TestCase):
    """Unittest for the class City"""

    def test_pep8_state(self):
        """Tests that there is no PEP8 error"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, "Found code style errors (and warnings).")

    def test_class(self):
        """Tests if the name of the class is correct"""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_mother(self):
        """Tests if City inherits from BaseModel"""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")
