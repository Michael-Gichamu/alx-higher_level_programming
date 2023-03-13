#!/usr/bin/python3
def no_c(my_string):
    """
    removes al instances of "c" and "C" from string
    """
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]
    return (new_str)
