#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)
    if len_tuple_a < 2:
        if len_tuple_a == 0:
            my_tuple_a = (0, 0)
        else:
            my_tuple_a = (tuple_a[0], 0)
    else:
        my_tuple_a = (tuple_a[0], tuple_a[1])
    if len_tuple_b < 2:
        if len_tuple_b == 0:
            my_tuple_b = (0, 0)
        else:
            my_tuple_b = (tuple_b[0], 0)
    else:
        my_tuple_b = (tuple_b[0], tuple_b[1])
    a = my_tuple_a[0] + my_tuple_b[0]
    b = my_tuple_a[1] + my_tuple_b[1]
    my_tuple = (a, b)
    return my_tuple
