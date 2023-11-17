#!/usr/bin/python3
"""Unit testing for the Rectangle Module."""
import unittest
import doctest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test the Base Class."""

    def setUp(self):
        """Set up number of object to 0 before each test case."""
        pass
        Base._Base__nb_objects = 0

    def test_firstRectangle(self):
        """Test normal usage of the class."""
        r1 = Rectangle(6, 4)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 5, 4)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(8, 6, 6, 8)
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 6)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 8)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(5, 5, 3, 3, 13)
        r4.width = 55
        r4.height = 34
        r4.x = 8
        r4.y = 9
        self.assertEqual(r4.width, 55)
        self.assertEqual(r4.height, 34)
        self.assertEqual(r4.x, 8)
        self.assertEqual(r4.y, 9)
        self.assertEqual(r4.id, 13)
        del r1, r2, r3, r4

    def test_raises(self):
        """Test wrong usage of the class."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(2)


    def test_width_validation(self):
        """Test invalid values of the width of the rectangle"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(6.5, "4.5")
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("6", 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle((6,), 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(True, 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle([6], 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle({"width" : 6}, 4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(int, 4)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-6, 4)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 4)

    def test_height_validation(self):
        """Test invalid values of the height of the rectangle"""
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, 6.5)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r = Rectangle(5, 6)
            r.height = 6.4
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, "6")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, (6,))
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, None)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, True)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, [6])
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, {"height" : 6})
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(5, int)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(5, -6)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(5, 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Rectangle(5, 9)
            r.height = -6

    def test_xy_validation(self):
        """Test the validation of coordinates."""
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, "zero")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(6, 4, 3, "same as x")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, (3, 3))
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, [3, 3])
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, {"x": 3, "y": 3})
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, int)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(6, 4, 3.5, 5.3)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(6, 4, 3, 5.3)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(6, 4, -5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(6, 4, 5, -4)
    
    def test_area(self):
        """Test the area method."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        r = Rectangle(1, 6)
        self.assertEqual(r.area(), 6)
        r = Rectangle(1, 1, 1, 1, 33)
        self.assertEqual(r.area(), 1)

    def test_display(self):
        """Test the display method.

        >>> r = Rectangle(5, 6)
        >>> r.display()
        #####
        #####
        #####
        #####
        #####
        #####
        >>> r.height = 2
        >>> r.display()
        #####
        #####
        >>> del r
        >>> r = Rectangle(3, 3, 2, 2)
        >>> r.display()
        <BLANKLINE>
        <BLANKLINE>
          ###
          ###
          ###
        >>> del r
        >>> r = Rectangle(3, 2, 3)
        >>> r.display()
           ###
           ###
        >>> del r
        >>> r = Rectangle(3, 2, 0, 3)
        >>> r.display()
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        ###
        ###
        >>> del r
        """
        finder = doctest.DocTestFinder()
        suite = doctest.DocTestSuite(test_finder=finder)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def test__str__(self):
        """Test __str__ representation of the class."""
        r1 = Rectangle(6, 4, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 6/4")
        r1.height = 8
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 6/8")
        r2 = Rectangle(5, 7, 5)
        self.assertEqual(str(r2), "[Rectangle] (1) 5/0 - 5/7")
        r2.y = r2.x
        self.assertEqual(str(r2), "[Rectangle] (1) 5/5 - 5/7")
        r3 = Rectangle(3, 9)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 3/9")
        r4 = Rectangle(5, 5, 5, 5, 5)
        self.assertEqual(str(r4), "[Rectangle] (5) 5/5 - 5/5")
        del r1, r2, r3, r4

    def test_update(self):
        """First test of the update method that updates the class attributes."""
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")
        r.update(11)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 10/10")
        r.update(11, 12)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 12/10")
        r.update(11, 12, 13)
        self.assertEqual(str(r), "[Rectangle] (11) 10/10 - 12/13")
        r.update(11, 12, 13, 14)
        self.assertEqual(str(r), "[Rectangle] (11) 14/10 - 12/13")
        r.update(11, 12, 13, 14, 15)
        self.assertEqual(str(r), "[Rectangle] (11) 14/15 - 12/13")
        r.update(11, 2, 3, 4, 5, 6, 7, 8, "best", {"school": 98})
        self.assertEqual(str(r), "[Rectangle] (11) 4/5 - 2/3")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(11, 12, 13, (14, 5))
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(11, [12, 13])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(11, -12, [12, 13])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(11, 0, [12, 13])
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r.update(11, 12, 13, 14, -15)
        del r

    def test_update2(self):
        """Second test of the update method that updates the class attributes."""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")
        r.update(coords=(33, 12), area=2, betty="best", x=2, dimentions=[20, 50])
        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 4/2")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(x= 1.5, height=2, y=3, width=4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(x= 1, height=(2,), y=3, width="4")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(x= 1, height=(2,), y=3, width=4)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(width = [2, 3, 5])
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r.update(width = -2, height = 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r.update(width=2, height=0)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r.update(width = 2, x = -3)
        del r
