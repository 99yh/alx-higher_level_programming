#!/usr/bin/python3
"""A rectangle model based on the Base model."""
from models import base


class Rectangle(base.Base):
    """Create a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Make a new rectangle instence."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def number_validator(name, value, min=0):
        """Validate values before using it."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < min:
            raise ValueError(f"{name} must be >{'' if min else '='} 0")

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle to a specefic value."""
        self.number_validator("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle to a specefic value."""
        self.number_validator("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coord of the rectangle to a specefic value."""
        self.number_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coord of the rectangle to a specefic value."""
        self.number_validator("y", value)
        self.__y = value

    def area(self):
        """Get the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle in stdout."""
        row = self.x * " " + self.width * "#" + '\n'
        col = row * self.height
        print(self.y * '\n' + col, end="")

    def __str__(self):
        """Represent the calss in an informal way."""
        repr = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        repr += f" - {self.width}/{self.height}"
        return repr

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        if not args:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "height" in kwargs:
                self.height = kwargs['height']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Get a dictionary represtation of the Rectangle object."""
        data = {'id': self.id, 'width': self.width, 'height': self.height}
        data['x'] = self.x
        data['y'] = self.y
        return data
