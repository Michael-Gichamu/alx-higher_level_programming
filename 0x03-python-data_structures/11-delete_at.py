#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list.
    """
    len_list = len(my_list)
    if len_list == 0:
        return None
    if idx < 0 or idx > (len_list - 1):
        return my_list
    del my_list[idx]
    return my_list
