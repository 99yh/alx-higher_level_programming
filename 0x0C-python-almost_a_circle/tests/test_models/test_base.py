#!/usr/bin/python3
"""Test Module for the base Module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the Base Class."""
    def setUp(self):
        """Set the tests up."""
        pass

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

    def test_raises(self):
        """Test wrong usage of the class."""
        pass
