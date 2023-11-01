#!/usr/bin/python3
"""Unit Test for ``max_integer`` function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the max_integer unit."""
    def test_legit(self):
        """Test with normal test cases."""
        self.assertEqual(max_integer([0, 0, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3]), 4)
        self.assertEqual(max_integer([-1, -4, -3]), -1)
        self.assertEqual(max_integer([1, 5, -9, 3, 5]), 5)
        self.assertEqual(max_integer([0]), 0)

    def test_edges(self):
        """Test with edge test cases."""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
