#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square"""

    def _init_(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
            """
            self.size = size
            self.position = position

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self._size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size - value

    @property
    def position(self):
        """Get/set the current position of the squuare."""
        return(self._position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        """Return the current area of the square."""
        return (self._size * self._size)

    def my_print(self):
        """Print the square with the # character"""
        if sefl._size == 0:
            print("")
            return

        [print("") for i in range(0, self._position[1])]
        for i in range(0, self._size):
            [print(" ", end= "") for j in range(0, self._position[0])]
            [print("#", end= "") for k in range(0, self._size)]
            print("")
