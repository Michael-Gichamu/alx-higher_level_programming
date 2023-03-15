#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list0 = []
    len_list = 0
    for key in a_dictionary.keys():
        key_list0.append(key)
        len_list += 1
    key_list = sorted(key_list0)
    for i in range(len_list):
        print("{}: {}".format(key_list[i], a_dictionary.get(key_list[i])))
