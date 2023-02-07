#!/usr/bin/python3
"""
Mylist class modudle.

Define MyList class.
"""


class MyList(list):
    """Define a MyList."""

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
