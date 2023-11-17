#!/usr/bin/python3
"""Square module based on the rectangle module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Make a new square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square (width or height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Represent the calss in an informal way."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        if not args:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.size = kwargs['size']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Get a dictionary represtation of the Rectangle object."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
