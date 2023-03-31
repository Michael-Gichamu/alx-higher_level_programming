#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer
    Returns True if value has been correctly printed(means value is integer)
    otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
