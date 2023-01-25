#!/usr/bin/python3
"""Define a class Square"""

class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
            positive (int, int): the position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
