#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    add_set = 0
    for element in my_set:
        add_set += element
    return add_set
