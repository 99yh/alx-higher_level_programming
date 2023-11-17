#!/usr/bin/python3
"""Test Module for the base Module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the Base Class."""

    def setUp(self):
        """Set up number of object to 0 before each test case."""
        Base._Base__nb_objects = 0

    def test_normal(self):
        """Test normal usage of the class."""
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 3)
        del b1, b2, b3, b4
