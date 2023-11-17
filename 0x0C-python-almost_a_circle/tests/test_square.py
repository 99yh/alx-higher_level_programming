#!/usr/bin/python3
"""Testing the Square Module."""
import unittest
import doctest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test the Base Class."""

    def setUp(self):
        """Set up number of object to 0 before each test case."""
        pass
        Base._Base__nb_objects = 0

    def test_sqares(self):
        """Testing normal usage of the class."""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.area(), 25)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 5")
        sq.size = 4
        self.assertEqual(sq.size, 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            sq.size = "XL"

    def test_raises(self):
        """Test wrong usage of the class."""
        with self.assertRaises(TypeError):
            Square()
