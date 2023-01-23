#!/usr/bin/python3

def saf_print_integer(value):
    """Print and integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        if a TypeError or ValueError occurs - False
        Otherwise - True
    """
    try:
        print("{:d}".format(value))

        return (True)
    except (TypeError, ValueError):
        return (False)
