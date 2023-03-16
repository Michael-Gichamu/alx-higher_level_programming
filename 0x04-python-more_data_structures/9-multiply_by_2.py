#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = dict(a_dictionary)
    for key, value in new_d.items():
        new_d[key] = value * 2
    return new_d
